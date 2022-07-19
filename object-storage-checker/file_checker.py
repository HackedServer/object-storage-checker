import asyncio
import json
import os
from urllib.parse import urlparse

import aiohttp
import pycountry
import yaml

import .globalping as gp
from s3_url import get_url
from write_metrics import write_to_influxdb


async def check_file(url: str, continent: str, session: aiohttp.ClientSession) -> dict:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    protocol = parsed_url.scheme
    body = gp.DEFAULT_BODY.copy()
    body["measurement"]["target"] = domain
    body["measurement"]["query"]["path"] = path
    body["measurement"]["query"]["protocol"] = protocol
    body["locations"] = [{"type": "continent", "value": continent}]

    async with session.post(f"https://{gp.DOMAIN_NAME}{gp.ApiPath.MEASUREMENTS.value}", json=body) as response:
        r = await response.json()
        request_id = r["id"]
    for _ in range(10):
        async with session.get(f"https://{gp.DOMAIN_NAME}{gp.ApiPath.MEASUREMENTS.value}/{request_id}") as response:
            r = await response.json()
            if r["status"] == gp.Status.FINISHED.value:
                # if "ETIMEDOUT" in r["results"][0]["result"]["rawOutput"]:
                #    raise Exception("CaughtTimeout")
                return {"url": url} | r["results"][0]
            else:
                await asyncio.sleep(1)


async def main():
    test_files: list[dict[str, str]] = []
    for file in os.listdir("./data/"):
        if file.endswith(".yaml") and not file == "example.yaml":
            with open(os.path.join(".", "data", file)) as f:
                data = yaml.safe_load(f)
                for i in data["files"]:
                    test_files.append({**i, **data["provider"]})

    session = aiohttp.ClientSession()
    coros = [
        check_file(
            file["object"]["url"] if file["object"].get("url") else await get_url(file["object"]),
            file["region"]["continent"],
            session,
        )
        for file in test_files
    ]

    for completed in asyncio.as_completed(coros):
        i = await completed

        print(
            json.dumps(
                {
                    "url": i["url"],
                    "status_code": i["result"]["statusCode"],
                    "total_time_ms": i["result"]["timings"]["total"],
                    "probe_location": "{}, {}, {}".format(
                        i["probe"]["city"].capitalize(),
                        pycountry.countries.get(alpha_2=i["probe"]["country"]).name,
                        i["probe"]["continent"],
                    ),
                },
                indent=4,
            )
        )

    await session.close()


if __name__ == "__main__":
    asyncio.run(main())

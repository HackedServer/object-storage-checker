from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import ASYNCHRONOUS
from influxdb_client.domain.write_precision import WritePrecision

idb_client = InfluxDBClient(
    url="",
    token="",
    org="",
)


async def write_to_influxdb(results):
    bucket = "object-status"
    write_api = idb_client.write_api(write_options=ASYNCHRONOUS)
    records = []
    for result in results:
        event = {
            "measurement": "object-status",
            "tags": {
                "company": result["company"],
                "service": result["service"],
                "product": result["product"],
                "region": result["object"]["region"],
            },
            "fields": {
                "timing_total": result["result"]["timings"]["total"],
                "result": result["result"]["statusCode"],
            },
        }
        records.append(Point.from_dict(event, write_precision=WritePrecision.S))

    write_api.write(bucket=bucket, record=records)

import aioboto3


async def get_url(object: dict[str, str]) -> str:
    session = aioboto3.Session()
    async with session.client(
        "s3",
        endpoint_url=object["endpoint_url"],
        aws_access_key_id=object["access_key"],
        aws_secret_access_key=object["secret_key"],
        region_name=object["region"],
    ) as s3:
        return await s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": object["bucket"], "Key": object["key"]},
            ExpiresIn=60,
        )

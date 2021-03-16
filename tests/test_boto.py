import boto3
from botocore.config import Config


def test_get_object_body() -> None:
    s3 = boto3.client(
        "s3", config=Config(retries={"mode": "standard", "max_attempts": 10})
    )
    obj = s3.get_object(Bucket="", Key="")
    assert "Body" in obj
    data = obj["Body"].read()
    print(data)

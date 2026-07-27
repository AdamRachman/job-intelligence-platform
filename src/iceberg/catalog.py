import os

from pyiceberg.catalog import load_catalog


catalog = load_catalog(
    "default",

    type="rest",

    uri=os.getenv(
        "ICEBERG_URI",
        "http://localhost:8181"
    ),

    warehouse="s3://warehouse",

    **{

        "s3.endpoint": os.getenv(
            "S3_ENDPOINT",
            "http://localhost:9000"
        ),

        "s3.access-key-id": "admin",

        "s3.secret-access-key": "password",

        "s3.region": "us-east-1",

        "s3.path-style-access": "true",

    }
)
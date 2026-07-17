from pyiceberg.catalog import load_catalog


catalog = load_catalog(
    "default",
    type="rest",
    uri="http://localhost:8181",
    warehouse="s3://warehouse",

    **{
        "s3.endpoint": "http://localhost:9000",
        "s3.access-key-id": "admin",
        "s3.secret-access-key": "password",
        "s3.region": "us-east-1",

        # Required for MinIO
        "s3.path-style-access": "true",
    }
)
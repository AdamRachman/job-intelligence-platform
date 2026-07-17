from pyiceberg.schema import Schema
from pyiceberg.types import (
    NestedField,
    StringType,
)

from src.schema.bronze_job_schema import JOB_SCHEMA


def build_bronze_schema():

    fields = []

    for field_id, field_name in enumerate(JOB_SCHEMA.keys(), start=1):

        fields.append(
            NestedField(
                field_id=field_id,
                name=field_name,
                field_type=StringType(),
                required=False,
            )
        )

    return Schema(*fields)
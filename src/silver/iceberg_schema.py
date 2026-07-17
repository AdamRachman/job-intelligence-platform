from pyiceberg.schema import Schema
from pyiceberg.types import (
    NestedField,
    StringType,
    LongType,
)

from src.schema.silver_job_schema import JOB_SCHEMA


def build_silver_schema():

    fields = []

    for field_id, field_name in enumerate(
        JOB_SCHEMA.keys(),
        start=1,
    ):

        # ==========================================
        # Numeric Fields
        # ==========================================

        if field_name in (
            "salary_min",
            "salary_max",
        ):

            field_type = LongType()

        # ==========================================
        # Default
        # ==========================================

        else:

            field_type = StringType()

        fields.append(

            NestedField(
                field_id=field_id,
                name=field_name,
                field_type=field_type,
                required=False,
            )

        )

    return Schema(*fields)
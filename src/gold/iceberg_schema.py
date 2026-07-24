from pyiceberg.schema import Schema
from pyiceberg.types import (
    NestedField,
    StringType,
    ListType,
    LongType,
)

from src.schema.gold_job_schema import JOB_SCHEMA


def build_gold_schema():

    fields = []


    for field_id, field_name in enumerate(
        JOB_SCHEMA.keys(),
        start=1,
    ):


        if field_name in [
            "salary_min",
            "salary_max",
        ]:

            field_type = LongType()


        elif field_name == "required_skills":

            field_type = ListType(

                element_id=field_id + 100,

                element_type=StringType(),

            )


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
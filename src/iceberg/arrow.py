import pyarrow as pa

from pyiceberg.types import (
    StringType,
    LongType,
    ListType,
)


def dataframe_to_arrow(df, iceberg_schema):

    fields = []

    for field in iceberg_schema.fields:

        if isinstance(field.field_type, StringType):

            arrow_type = pa.string()


        elif isinstance(field.field_type, LongType):

            arrow_type = pa.int64()


        elif isinstance(field.field_type, ListType):

            # Support list<string>
            if isinstance(
                field.field_type.element_type,
                StringType,
            ):

                arrow_type = pa.list_(
                    pa.field(
                        "element",
                        pa.string(),
                        nullable=False,
                    )
                )

            else:

                raise TypeError(
                    f"Unsupported List element type: {field.field_type.element_type}"
                )


        else:

            raise TypeError(
                f"Unsupported Iceberg type: {field.field_type}"
            )


        fields.append(

            pa.field(
                field.name,
                arrow_type,
                nullable=True,
            )

        )


    arrow_schema = pa.schema(fields)


    return pa.Table.from_pandas(

        df,

        schema=arrow_schema,

        preserve_index=False,

    )
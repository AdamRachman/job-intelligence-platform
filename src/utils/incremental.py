import pandas as pd


def get_existing_keys(table, business_keys):

    try:

        df = table.scan().to_pandas()

        if df.empty:
            return set()

        return set(
            map(
                tuple,
                df[business_keys].values
            )
        )

    except Exception:
        return set()


def filter_incremental(
    df,
    table,
    business_keys,
):

    existing_keys = get_existing_keys(
        table,
        business_keys,
    )

    df = df.copy()

    df["_business_key"] = list(
        map(
            tuple,
            df[business_keys].values
        )
    )

    new_df = (
        df[
            ~df["_business_key"].isin(existing_keys)
        ]
        .drop(columns="_business_key")
        .copy()
    )

    return new_df
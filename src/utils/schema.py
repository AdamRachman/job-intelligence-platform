import pandas as pd


def enforce_schema(df):

    df = df.copy()

    for col in df.columns:

        df[col] = (
            df[col]
            .astype("object")
            .where(
                pd.notna(df[col]),
                None
            )
        )

    return df
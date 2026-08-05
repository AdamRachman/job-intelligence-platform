from trino.dbapi import connect

from src.config.settings import (
    TRINO_HOST,
    TRINO_PORT,
    TRINO_USER,
    TRINO_CATALOG,
    TRINO_SCHEMA,
)


# ======================
# Trino Connection
# ======================

def get_trino_connection():

    return connect(
        host=TRINO_HOST,
        port=TRINO_PORT,
        user=TRINO_USER,
        catalog=TRINO_CATALOG,
        schema=TRINO_SCHEMA,
    )
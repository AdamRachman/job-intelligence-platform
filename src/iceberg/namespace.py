from pyiceberg.exceptions import NamespaceAlreadyExistsError


def ensure_namespace(catalog, namespace: str) -> None:
    """
    Create namespace if it does not already exist.
    Equivalent to:
        CREATE SCHEMA IF NOT EXISTS <namespace>
    """

    try:

        catalog.create_namespace(namespace)

        print(f"Namespace '{namespace}' created.")

    except NamespaceAlreadyExistsError:

        print(f"Namespace '{namespace}' already exists.")
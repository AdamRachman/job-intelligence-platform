from src.linkedin.connector import LinkedInConnector
from src.jobstreet.connector import JobStreetConnector


# ==========================================================
# CONNECTOR REGISTRY
# ==========================================================

CONNECTOR_REGISTRY = {

    "linkedin": LinkedInConnector(),

    "jobstreet": JobStreetConnector(),

}
from src.ai.client import get_llm
from src.ai.parser import AIEnrichment
from src.ai.prompt import PROMPT


llm = get_llm().with_structured_output(
    AIEnrichment
)


def enrich_job(title, description):

    chain = PROMPT | llm

    response = chain.invoke(
        {
            "title": title,
            "description": description,
        }
    )

    return response
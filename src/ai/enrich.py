from src.ai.client import get_llm
from src.ai.parser import AIEnrichment
from src.ai.prompt import PROMPT


llm = get_llm().with_structured_output(
    AIEnrichment
)


import time


def enrich_job(title, description):

    chain = PROMPT | llm


    for attempt in range(3):

        try:

            response = chain.invoke(
                {
                    "title": title,
                    "description": description[:4000],
                }
            )

            return response


        except Exception as e:

            print(
                f"AI enrichment failed attempt {attempt+1}/3"
            )

            print(e)

            time.sleep(5)


    return AIEnrichment()
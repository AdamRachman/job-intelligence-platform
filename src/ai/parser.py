from typing import List

from pydantic import BaseModel, Field


class AIEnrichment(BaseModel):

    seniority_level: str = Field(
        default="Unknown",
        description="Job seniority level. Allowed values: Entry Level, Associate, Mid-Senior Level, Unknown."
    )

    required_skills: List[str] = Field(
        default_factory=list,
        description="List of concrete technical skills such as programming languages, frameworks, databases, cloud platforms, infrastructure tools, and engineering tools."
    )
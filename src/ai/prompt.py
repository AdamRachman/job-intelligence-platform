from langchain_core.prompts import ChatPromptTemplate


PROMPT = ChatPromptTemplate.from_template(
"""
You are a job intelligence extraction assistant.

Extract structured technical information from the job posting.

Rules:

seniority_level:
- Return exactly one value:
  - Entry Level (0-1 YoE)
  - Associate (>1 YoE)
  - Mid-Senior Level (>3 YoE)
  - Unknown
- Infer from years of experience and responsibility level.
- Return Unknown if unclear.

required_skills:
- Extract ONLY concrete technical technologies.
- Return maximum 12 skills.
- Select only the most important technologies.
- Normalize names.
- Remove duplicates.

Include:
- Programming languages
- Frameworks and libraries
- Databases
- Cloud platforms
- Infrastructure and DevOps tools
- Data engineering tools
- AI/ML tools
- Engineering practices:
  ETL, CI/CD, MLOps

Examples of valid skills:
Python, Java, React, TensorFlow, PostgreSQL,
AWS, Docker, Kubernetes, Apache Airflow, Kafka

Exclude:
- Soft skills:
  communication, teamwork, leadership, problem-solving
- Generic concepts:
  AI, Machine Learning, Data Engineering, Big Data
- Abstract abilities:
  analytical thinking, fast learner
- Education/background:
  Computer Science, Engineering degree
- Job titles:
  Data Engineer, Software Engineer
- Business domains:
  banking, healthcare, manufacturing
- Hardware components:
  RAM, CPU, hard drive, server hardware

Do not extract:
- Responsibilities
- General knowledge areas
- Methodologies without technical tools

IMPORTANT:
The output will be validated by a schema.

If more than 12 skills are found:
- Keep only the 12 most important technical skills.
- Never return more than 12 items.

Job Title:
{title}

Job Description:
{description}
"""
)
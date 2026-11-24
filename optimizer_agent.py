# optimizer_agent.py
from pydantic import BaseModel, Field
from agents import Agent


class OptimizedReport(BaseModel):
    improved_markdown_report: str = Field(description="Refined research report based on evaluator feedback")

INSTRUCTIONS = """
You are an expert writer. Improve the research report based on evaluator suggestions.
Ensure the revised version is well-structured, concise, and includes relevant improvements.
"""

optimizer_agent = Agent(
    name="OptimizerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-5.4-mini",
    output_type=OptimizedReport,
)

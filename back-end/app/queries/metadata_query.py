from typing import Any, Type
from app.models.metadata_llm import MetadataLLM
from app.queries.base import BaseQuery


class MetadataQuery(BaseQuery):
    text: str
    filename: str
    response_model: Type[Any] = MetadataLLM
    prompt: str = (
        "Extract the <actors>, <summary>, <label>, <tags>, <is_company_wide_doc> from the provided text into your response."
        "Limit the number of tags to 10."
        "Use the following definition of terms to provide the most accurate responses."
        """<actors>Actors are any parties involved in the text this may include the text author and any other stakeholders involved</actors>
            <label>
                The label specifies the domain of the document given the following label types:
                1. career-framework: A set of guidelines outlining roles, competencies, and career paths within an organization.
                2. company-performance-review-process: Standardized procedures for assessing and evaluating employee performance.
                3. company-values: Fundamental beliefs and principles guiding a company's culture and actions.
                4. personal-performance-review: An evaluation focusing on an individual's personal goals, achievements, and areas for improvement.
                5. manager-performance-review: An assessment of a manager's leadership abilities and team effectiveness.
                6. one-on-one: A private meeting between two individuals, typically a manager and an employee, for communication and feedback.
                7. unknown: A placeholder for items whose specific type or classification is not determined.
            </label>
            <tags>Keywords which best describe the document. limit the number of tags to 10</tags>
            <is_company_wide_doc>
                Specifies whether this document can be shared company wide or should remain private.
                personal-performance-review, manager-performance-review, one-on-one, and unknown documents should always remain private
            </is_company_wide_doc>"""
    )

    def get_message_content(self) -> str:
        return f"{self.prompt} provided the following text <text>{self.text}</text>. filename: {self.filename}."

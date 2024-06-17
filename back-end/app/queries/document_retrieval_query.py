from app.queries.base import BaseQuery
from typing import Any, Type, List
from app.models.document import DocumentLabelEnum
from pydantic import BaseModel, Field

class DocumentResults(BaseModel):
    file_name: str = Field(default=None, description='the document file name')

class DocumentRetrievalQuery(BaseQuery):
    documents: str = None
    prompt: str = (
        "Based on the user question provided please select the relevant document which the user needs to proceed"
        "use the following documents to pick out the most relevant"
    )
    response_model: Any = DocumentResults

    def get_message_content(self) -> str:
        return f"{self.prompt} given the following documents: {self.documents}"
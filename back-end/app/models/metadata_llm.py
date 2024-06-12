from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date, datetime
from app.models.document import DocumentLabelEnum, DocumentTypeEnum, DocumentSourceEnum


class MetadataLLM(BaseModel):
    """Metadata LLM pydantic model. Generates prompts and calls llm for metadata results"""
    actors: Optional[List[str]] = Field(
        default=None, description="Unique actors in this document."
    )
    summary: str = Field(
        ..., description="A comprehensive summary of this document."
    )
    label: DocumentLabelEnum = Field(
        ..., description="Correctly assign one of the predefined labels to the document."
    )
    tags: List[str] = Field(
        ..., description="Max of 10 Keywords associated with this document.",
        max_items=10
    )
    source: DocumentSourceEnum = Field(
        default=DocumentSourceEnum.upload, description="The source from which this document was obtained."
    )
    is_company_wide_doc: bool = Field(
        ..., description="Indicates if this document is intended for company wide distribution."
    )
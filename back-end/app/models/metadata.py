import os
from pydantic import BaseModel, Field
from typing import List, Optional, Any
from app.models.document import DocumentLabelEnum, DocumentTypeEnum, DocumentSourceEnum
from app.clients.pocketbase import pb

class Metadata(BaseModel):
    id: Optional[str] = None
    document_id: str
    actors: Optional[List[str]] = None
    summary: str
    label: DocumentLabelEnum
    tags: List[str]
    source: DocumentSourceEnum
    is_company_wide_doc: bool
    file_extension: DocumentTypeEnum

    def save_record(self) -> Any:
        record = pb.collection('metadata').create({
            'document_id': self.document_id,
            'actors': self.actors,
            'summary': self.summary,
            'label': self.label.value,
            'tags': self.tags,
            'source': self.source.value,
            'is_company_wide_doc': self.is_company_wide_doc,
            'file_extension': self.file_extension.value
        })
        return record

    @classmethod
    def get_file_extension(cls, filename:str) -> str:
        _, file_extension = os.path.splitext(filename)
        return file_extension.lstrip('.')
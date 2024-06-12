import os
from enum import Enum
from typing import Optional, Any
from app.clients.pocketbase import pb
from pydantic import BaseModel


class DocumentLabelEnum(Enum):
    career_framework = 'career-framework'
    company_performance_review_process = 'company-performance-review-process'
    company_values = 'company-values'
    personal_performance_review = 'personal-performace-review'
    manager_performance_review = 'manager-performance-review'
    one_on_one = 'one-on-one'
    unknown = 'unknown'

class DocumentTypeEnum(Enum):
    txt = 'txt'
    pdf = 'pdf'
    doc = 'doc'
    docx = 'docx'
    xls = 'xls'
    xlsx = 'xlsx'
    ppt = 'ppt'
    pptx = 'pptx'
    csv = 'csv'

class DocumentSourceEnum(Enum):
    upload = 'upload'
    slack = 'slack'
    google_drive = 'google-drive'
    notion = 'notion'
    lattice = 'lattice'


class Document(BaseModel):
    id: Optional[str] = None
    text: str
    file_name: str

    def save_record(self) -> Any:
        record = pb.collection('documents').create({
            'text': self.text,
            'file_name': self.file_name
        })
        self.id = record.id
        return record
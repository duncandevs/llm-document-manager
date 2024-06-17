from pydantic import BaseModel
from typing import Type, Any
from app.clients.instructor import instructorClient

class DocumentIDResponse(BaseModel):
    document_id: str


class SimpleResponse(BaseModel):
    response: str

def llm_get_document_id(prompt:str):
    return instructorClient.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            response_model=DocumentIDResponse,
            max_retries=3
        )

def llm_get_query_response(prompt:str):
    return instructorClient.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            response_model=SimpleResponse,
            max_retries=3
        )


class BaseQuery(BaseModel):
    model: str = "gpt-3.5-turbo-0125"
    response_model: Any
    max_retries: int = 3

    class Config:
        arbitrary_types_allowed = True

    def get_message_content(self) -> str:
        raise NotImplementedError("Subclasses should implement this method to construct the message content")

    def call_llm(self) -> Any:
        message_content = self.get_message_content()
        result = instructorClient.chat.completions.create(
            model=self.model,
            messages=[{
                "role": "user",
                "content": message_content
            }],
            response_model=self.response_model,
            max_retries=self.max_retries
        )
        return result
from pydantic import BaseModel
from typing import Type, Any
from app.clients.instructor import instructorClient

class BaseQuery(BaseModel):
    model: str = "gpt-3.5-turbo-0125"
    response_model: Type[Any]
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
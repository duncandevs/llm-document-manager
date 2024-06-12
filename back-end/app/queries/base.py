from pydantic import BaseModel
from typing import Type, Any
from app.clients.instructor import instructorClient

class BaseQuery(BaseModel):
    model: str = "gpt-4"
    response_model: Type[Any]  # Type hint for the response model

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
            response_model=self.response_model
        )
        return result
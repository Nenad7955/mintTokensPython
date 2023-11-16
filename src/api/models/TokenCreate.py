from pydantic import BaseModel


class TokenCreate(BaseModel):
    media_url: str
    owner: str

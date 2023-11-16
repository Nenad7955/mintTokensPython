from pydantic import BaseModel


class TokenCreateResponse(BaseModel):
    id: str
    media_url: str
    owner: str
    unique_hash: str
    tx_hash: str

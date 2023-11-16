from fastapi import APIRouter

from src.api.models.TokenCreate import TokenCreate
from src.api.models.TokenCreateResponse import TokenCreateResponse


class TokenController:
    def __init__(self, tokenService):
        self.tokenService = tokenService

        self.router = APIRouter(
            prefix='/tokens',
        )

        self.router.add_api_route(
            methods=['POST'],
            path='/create',
            endpoint=self.post_create
        )

        self.router.add_api_route(
            methods=['GET'],
            path='/list',
            endpoint=self.get_list
        )

        self.router.add_api_route(
            methods=['GET'],
            path='/total_supply',
            endpoint=self.get_total_supply
        )

    async def post_create(self, token: TokenCreate) -> TokenCreateResponse:
        token_id, unique_hash, tx_hash = await self.tokenService.mint_token(
            media_url=token.media_url,
            owner=token.owner,
        )

        return TokenCreateResponse(
            id=token_id,
            media_url=token.media_url,
            owner=token.owner,
            unique_hash=unique_hash,
            tx_hash=tx_hash,
        )

    async def get_list(self):
        return {"result": await self.tokenService.get_tokens_list()}

    async def get_total_supply(self):
        return {"result": self.tokenService.get_tokens_supply()}

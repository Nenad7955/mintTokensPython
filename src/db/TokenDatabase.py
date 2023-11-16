from prisma import Prisma


class TokenDatabase:
    def __init__(self, prisma: Prisma):
        self.prisma = prisma

    async def save_token(self, token_id, media_url, owner, unique_hash, tx_hash):
        return await self.prisma.token.create(
            data={
                "id": token_id,
                "media_url": media_url,
                "owner": owner,
                "unique_hash": unique_hash,
                "tx_hash": tx_hash,
            }
        )

    async def get_tokens(self):
        return await self.prisma.token.find_many()

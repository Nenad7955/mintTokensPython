import random
import string
import uuid


class TokenService:
    def __init__(self, db, token_contract):
        self.db = db
        self.token_contract = token_contract
        self.tokens = []

    async def mint_token(self, media_url: str, owner: str):
        unique_hash = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20))
        token_id = str(uuid.uuid4().hex)

        tx_hash = self.token_contract.mint_token(owner, unique_hash, media_url)
        await self.db.save_token(token_id, media_url, owner, unique_hash, tx_hash)
        return token_id, unique_hash, tx_hash

    def get_tokens_list(self):
        return self.db.get_tokens()

    def get_tokens_supply(self):
        return self.token_contract.get_total_supply()

from src.service.web3.ContractBase import ContractBase


class Contract(ContractBase):
    def __init__(self, web3, addr: str, public_key: str, private_key: str):
        super().__init__(web3, public_key, private_key)
        self.contract = self.web3.eth.contract(address=addr, abi=abi)

    def mint_token(self, owner, unique_hash, media_url):
        tx = (
            self.contract.functions.mint(owner, unique_hash, media_url)
            .build_transaction({
                "from": self.public_key, "nonce": self.get_nonce()
            }))
        # need to get tx_hash
        return self.send_tx(tx)

    def get_total_supply(self):
        return self.contract.functions.totalSupply().call()


# Can move to file... Should even...
abi = [
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view", "type": "function"},
    {
        "inputs": [{"internalType": "address", "name": "owner", "type": "address"},
                   {"internalType": "string", "name": "uniqueHash", "type": "string"},
                   {"internalType": "string", "name": "mediaURL", "type": "string"}],
        "name": "mint", "outputs": [],
        "stateMutability": "nonpayable", "type": "function"}
]

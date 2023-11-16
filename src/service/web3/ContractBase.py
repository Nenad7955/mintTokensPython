import json


class ContractBase:
    def __init__(self, web3, public_key: str, private_key: str):
        self.web3 = web3
        self.public_key = public_key
        self.private_key = private_key

    def send_tx(self, tx) -> str:
        signed_txn = self.web3.eth.account.sign_transaction(tx, self.private_key)
        it = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return str(it.hex())

    def get_nonce(self) -> int:
        return self.web3.eth.get_transaction_count(self.public_key)



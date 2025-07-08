# backend/wallets/withdraw.py

from web3 import Web3
import os

def withdraw_tokens(contract_address, private_key, to_address, amount_eth):
    w3 = Web3(Web3.HTTPProvider(os.getenv("ETH_NODE")))
    acct = w3.eth.account.from_key(private_key)

    erc20_abi = ["function transfer(address to, uint amount) public returns (bool)"]
    contract = w3.eth.contract(address=contract_address, abi=erc20_abi)

    tx = contract.functions.transfer(
        to_address,
        w3.toWei(amount_eth, "ether")
    ).build_transaction({
        "from": acct.address,
        "gas": 200000,
        "gasPrice": w3.toWei("50", "gwei"),
        "nonce": w3.eth.get_transaction_count(acct.address),
    })

    signed = acct.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    return tx_hash.hex()

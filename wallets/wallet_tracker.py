# backend/wallets/wallet_tracker.py

from web3 import Web3
import os

def check_wallet_balance(token_address, user_wallet):
    w3 = Web3(Web3.HTTPProvider(os.getenv("ETH_NODE")))
    erc20_abi = [{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf",
    "outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]

    contract = w3.eth.contract(address=token_address, abi=erc20_abi)
    balance = contract.functions.balanceOf(user_wallet).call()
    return w3.fromWei(balance, 'ether')

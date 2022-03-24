from brownie import accounts, network, config, Contract
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "hardhat",
    "development",
    "ganache-local",
    "mainnet-fork",
]

DECIMALS = 8
STARTING_PRICE = 411200000000


def get_publish_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[5]
    else:
        return accounts.add(config["wallets"]["publisher_key"])


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["personal_key"])

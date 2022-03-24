from brownie import network, config, FireAnEvent
from scripts.helpful_scripts import get_account


def fireAnEvent():
    publish_account = get_account()
    print(f"Account {publish_account}")

    # configure dependencies
    print(f"The active network is {network.show_active()}")

    contract = FireAnEvent[-1]
    print(f"Contract {contract}")

    tx = contract.fireEvent({"from": publish_account})

    print(tx.events)
    print()
    print(tx.events["TestEvent"])
    print()
    print(tx.events["TestEvent"]["number"] > 0)


def main():
    fireAnEvent()

from brownie import network, config, FireAnEvent
from scripts.helpful_scripts import get_publish_account


def deploy():
    publish_account = get_publish_account()
    print(f"Account {publish_account}")

    # configure dependencies
    print(f"The active network is {network.show_active()}")

    print("Deploying..")
    deployed_contract = FireAnEvent.deploy(
        {"from": publish_account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Deployed: {deployed_contract}")
    return deployed_contract


def main():
    deploy()

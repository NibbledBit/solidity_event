import pytest
from brownie import network, config
from scripts.deploy import deploy

# import the following dependencies
import json
from web3 import Web3
import asyncio

from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_publish_account,
)


def test_deploy_contract():
    if network.show_active() != "rinkeby":
        pytest.skip("only for Rinkeby testing.")
    deployed_contract = deploy()


def test_fire_event():
    if network.show_active() != "rinkeby":
        pytest.skip("only for Rinkeby testing.")

    publish_account = get_publish_account()

    deployed_contract = deploy()

    tx = deployed_contract.fireEvent({"from": publish_account})

    assert tx.events["TestEvent"]["number"] > 0

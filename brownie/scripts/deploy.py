from turtle import update
from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    account = accounts[0]
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)

    simple_value = simple_storage.retrieve()
    print(simple_value)

    tranasaction = simple_storage.store(15, {"from": account})
    tranasaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()

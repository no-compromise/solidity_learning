from brownie import FundMe, config
from scripts.helpfull_scripts import get_account


def deploy_fund_me():
    account = get_account()

    if network.show_active != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        pass
        # Tuto dokoncit

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=True,
    )
    print(f"Conttract deployed to: {fund_me.address} ")


def main():
    deploy_fund_me()

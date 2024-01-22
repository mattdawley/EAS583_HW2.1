import eth_account
from web3 import Web3
from eth_account.messages import encode_defunct


def sign(m):
    w3 = Web3()
    # create an eth account and recover the address (derived from the public key) and private key
    acct = eth_account.Account.create()


    eth_address = acct.address  # Eth account
    private_key = acct.key

    # generate signature
    signed_message = eth_account.sign_message(m, private_key = private_key)

    assert isinstance(signed_message, eth_account.datastructures.SignedMessage)

    return eth_address, signed_message

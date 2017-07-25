from bitcoin.Current.Objects import Transaction
import requests


class Address:
    def __init__(self, hash):
        self.hash = hash
        res = requests.get("https://test-insight.bitpay.com/api/addr/" + str(hash)).json()
        self.tx = res["transactions"]
        # Insert pass data if needed

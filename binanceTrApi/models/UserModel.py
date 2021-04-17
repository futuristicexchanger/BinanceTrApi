import hmac
from operator import itemgetter
import hashlib


class UserModel:
    def __init__(self, api, secret, test=False):
        self.api = api
        self.secret = secret
        if test:
            print("[UserModel] constructor called")
            self.tester()

    def tester(self):
        print(" YOUR API: " + self.api)
        print(" YOUR SECRET KEY: " + self.secret)
        testDict = {"testkey1": "testval1", "testkey2": "testval2"}
        print(self.generate_signature(testDict))
        print(self.order_params(testDict))

    def generate_signature(self, data):
        res = hmac.new(self.secret.encode("utf-8"), data.encode("utf-8"), hashlib.sha256)
        return res.hexdigest()

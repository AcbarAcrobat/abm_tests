import random
import requests
from utils.testdata import TestData


TeD = TestData()


class Helper:

    def get_id(self):
        return self.autorize().json()['result']['id']

    def tok3n(self):
        return self.autorize().json()["result"]["token"]

    def autorize(self):
        r = requests.post(TeD.url() + "/login", headers={"Content-Type": "application/json"},
                          json={"login": TeD.username(),
                                "password": TeD.password()})
        return r

    def random_value(self):
        v = random.randint(0, 999)
        print(v)
        return v

    def get_user_regions(self):
        r = requests.post(TeD.url() + "/user/regions", json={"token": self.tok3n()})
        group = r.json()["result"]["data"]
        int_group = []
        for i in group:
            try:
                int_val = int(i)
                if int_val != 0:
                    int_group.append(int_val)
            except Exception:
                pass
        foo = random.choice(int_group)
        print(foo)
        return foo

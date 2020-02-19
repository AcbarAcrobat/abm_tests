import requests
from truth.truth import AssertThat

from fixture.TestData import TestData
from support import config
import random


class TestApi(TestData):

    def get_token(self):
        return self.autorize().json()["result"]["get_token"]

    def autorize(self):
        r = requests.post(self.url() + "/login", headers={"Content-Type": "application/json"},
                          json={"login": self.username(),
                                "password": self.password()})
        return r

    def random_value(self):
        v = random.randint(0, 999)
        print(v)
        return v

    # def get_region(self, url=config.get("url")):
    #     a = self.autorize()
    #     get_token = a.json()["result"]["get_token"]
    #     r = requests.post(url + "/user/regions", json={"get_token": get_token})
    #     group = r.json()["result"]["data"]
    #     first_integer = next(filter(lambda i: i.isdigit(), group))
    #     foo = random.choice(first_integer)
    #     print(foo)
    #     return foo

    def get_region(self):
        r = requests.post(self.url() + "/user/regions", json={"get_token": self.get_token()})
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

    def get_id(self):
        return self.autorize().json()['result']['id']

    def test_validate_with_token(self):
        r = requests.post(self.url() + "/user", json={'get_token': self.get_token()})
        AssertThat(r.status_code).IsEqualTo(200)
        AssertThat(r.json()['result']).ContainsItem("roles", ["ROLE_ABM_ADMIN"])
        print(r)
        print(r.json())

    def test_correct_login_with_data(self):
        r = self.autorize()
        AssertThat(r.status_code).IsEqualTo(200)
        AssertThat(r.json()['result']).ContainsItem("roles", ["ROLE_ABM_ADMIN"])

    def test_incorrect_login_with_null(self):
        r = requests.post(self.url() + "/login", json={"login": "   ",
                                                       "password": "   "})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.status_code)

    def test_incorrect_login_with_data(self):
        r = requests.post(self.url() + "/login", json={"login": "123",
                                                       "password": "123"})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.status_code)

    def test_get_user_with_incorrect_token(self):
        r = requests.post(self.url() + "/user", json={"get_token": "3AED6F4648F581DEF6645C833DEFFC9B"})
        AssertThat(r.status_code).IsEqualTo(401)

    def test_get_user_with_token_null(self):
        r = requests.post(self.url() + "/user", json={"get_token": " "})
        AssertThat(r.status_code).IsEqualTo(401)

    def test_get_user_by_string_id(self):
        r = requests.post(self.url() + "/user/username", json={"get_token": self.get_token(),
                                                               "username": self.username()})
        print(r)

    def test_get_user_by_string_id_incorrect_user(self):
        v = self.autorize().json()["result"]["get_token"]
        r = requests.post(self.url() + "/user/username", json={"get_token": v,
                                                               "username": self.random_value()})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())

    def test_get_user_by_string_id_incorrect_token(self):
        r = requests.post(self.url() + "/user/username", json={"get_token": " %%%%%%%",
                                                               "username": self.username()})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())

    def test_get_user_by_string_id_with_null(self):
        r = requests.post(self.url() + "/user/username", json={"get_token": "  ",
                                                               "username": "  "})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())

    def test_get_user_by_string_id_and_token(self):
        r = requests.post(self.url() + "/user/id", json={"get_token": self.get_token(),
                                                         "id": self.get_id()})
        AssertThat(r.status_code).IsEqualTo(200)
        if 'roles' in r.json() and r.json()["result"]["roles"] != "5OLE_ABM_ADMIN":
            AssertionError and print("User with ID", r.json()['result']['id'], "is have not admin role")
        print(r)

    # def test_get_user_by_string_id_and_incorrect_token_max_int(self, url=config.get("url")):
    #     a = self.autorize()
    #     r = requests.post(url + "/user/id", json={"get_token": a.json()['result']['get_token'],
    #                                               "id": 9223372036854775807})
    #     assert r.status_code == 401
    #     print(r.json())

    def test_get_user_by_string_id_and_token_null(self):
        a = self.get_id()
        r = requests.post(self.url() + "/user/id", json={"get_token": " ",
                                                         "id": a})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r)

    # def test_get_user_by_null_id_and_correct_token(self, url=config.get("url")):
    #     a = self.autorize()
    #     r = requests.post(url + "/user/id", json={"get_token": a.json()['result']['get_token'],
    #                                               "id": 0})
    #     assert r.status_code == 401
    #     print(r)

    def test_get_regions_by_token(self):
        r = requests.post(self.url() + "/user/regions", json={"get_token": self.get_token()})
        AssertThat(r.status_code).IsEqualTo(200)
        print(r.json())
        print(r)

    def test_get_regions_by_incorrect_token(self):
        r = requests.post(self.url() + "/user/regions", json={"get_token": "3AED6F4648F581DGVZEF6645C833DEFFC9B"})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r)

    def test_get_regions_by_token_null(self):
        r = requests.post(self.url() + "/user/regions", json={"get_token": ""})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r)

    def test_get_workgroup_by_token_and_region(self):
        r = requests.post(self.url() + "/region/workgroup", json={"get_token": self.get_token(),
                                                                  "region": self.get_region()})
        AssertThat(r.status_code).IsEqualTo(200)
        print(r.json())
        print(r)

    def test_get_workgroup_by_incorrect_token_and_correct_region(self):
        r = requests.post(self.url() + "/region/workgroup", json={"get_token": "3AED6F4648F581DGVZEF6645C833DEFFC9BAAVGBBGY",
                                                                "region": self.get_region()})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())
        print(r)

    def test_get_workgroup_by_empty_token_and_correct_region(self):
        r = requests.post(self.url() + "/region/workgroup", json={"get_token": "                         ",
                                                                  "region": self.get_region()})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())
        print(r)

    def test_get_workgroup_by_incorrect_token_and_incorrect_region(self):
        r = requests.post(self.url() + "/region/workgroup", json={"get_token": "3AED6F4648F581DGVZEF6645C833DEFFC9BAAVGBBGY",
                                                                  "region": self.random_value()})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())
        print(r)

import pytest
from fixture.Application import Application
import requests
from truth.truth import AssertThat
from support import config
import random


class TestApi:

    def auth(self, login=config.get("login"), password=config.get("password"), url=config.get("url")):
        body = {"login": login,
                "password": password}
        r = requests.post(url + "/login", headers={"Content-Type": "application/json"},
                          json=body)
        return r

    def random_value(self):
        v = random.randint(0, 999)
        print(v)
        return v

    # def get_region(self, url=config.get("url")):
    #     a = self.auth()
    #     token_ = a.json()["result"]["token"]
    #     r = requests.post(url + "/user/regions", json={"token": token_})
    #     group = r.json()["result"]["data"]
    #     foo = random.choice(group)
    #     print(foo)
    #     return foo

    def get_region_lam(self, url = config.get("url")):
        a = self.auth()
        token_ = a.json()["result"]["token"]
        r = requests.post(url + "/user/regions", json={"token": token_})
        group = r.json()["result"]["data"]
        int_group = []
        for i in group:
            try:
                int_val = int(i)
                if int_val != 0:
                    int_group.append(int_val)
            except Exception:
                pass
        # first_integer = next(filter(lambda i: i.isdigit(), group))
        foo = random.choice(int_group)
        print(foo)
        return foo

    def test_validate_with_token(self, url=config.get("url")):
        r = self.auth()
        r = requests.post(url + "/user", json={'token': r.json()['result']['token']})
        AssertThat(r.json()['result']).ContainsItem("roles", ["ROLE_ABM_ADMIN"])
        print(r)
        print(r.json())

    def test_correct_login_with_data(self):
        r = self.auth()
        AssertThat(r.status_code).IsEqualTo(200)
        AssertThat(r.json()['result']).ContainsItem("roles", ["ROLE_ABM_ADMIN"])

    def test_incorrect_login_with_null(self):
        d = {"login": " ",
             "password": " "}
        r = requests.post(config.get('url') + "/login", json=d)
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.status_code)

    def test_incorrect_login_with_data(self):
        d = {"login": "123",
             "password": "123"}
        r = requests.post(config.get("url") + "/login", json=d)
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.status_code)

    def test_get_user_with_incorrect_token(self):
        d = {"token": "3AED6F4648F581DEF6645C833DEFFC9B"}
        r = requests.post(config.get("url") + "/user", json=d)
        AssertThat(r.status_code).IsEqualTo(401)

    def test_get_user_with_token_null(self):
        d = {"token": " "}
        r = requests.post(config.get("url") + "/user", json=d)
        AssertThat(r.status_code).IsEqualTo(401)

    def test_get_user_by_string_id(self, username=config.get("login"), url=config.get("url")):
        r = self.auth()
        r = requests.post(url + "/user/username", json={"token": r.json()["result"]["token"],
                                                        "username": username})
        print(r)

    def test_get_user_by_string_id_incorrect_user(self, url=config.get("url")):
        v = self.auth()
        r = requests.post(url + "/user/username", json={"token": v.json()["result"]["token"],
                                                        "username": self.random_value()})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())

    def test_get_user_by_string_id_incorrect_token(self, url=config.get("url")):
        r = requests.post(url + "/user/username", json={"token": " %%%%%%%",
                                                        "username": config.get("login")})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())

    def test_get_user_by_string_id_with_null(self, url=config.get("url")):
        r = requests.post(url + "/user/username", json={"token": "  ",
                                                        "username": "  "})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())

    def test_get_user_by_string_id_and_token(self, url=config.get("url")):
        a = self.auth()
        r = requests.post(url + "/user/id", json={"token": a.json()['result']['token'],
                                                  "id": a.json()['result']['id']})
        AssertThat(r.status_code).IsEqualTo(200)
        if 'roles' in r.json() and r.json()["result"]["roles"] != "5OLE_ABM_ADMIN":
            AssertionError and print("User with ID", a.json()['result']['id'], "is have not admin role")
        print(r)

    # def test_get_user_by_string_id_and_incorrect_token_max_int(self, url=config.get("url")):
    #     a = self.auth()
    #     r = requests.post(url + "/user/id", json={"token": a.json()['result']['token'],
    #                                               "id": 9223372036854775807})
    #     assert r.status_code == 401
    #     print(r.json())

    def test_get_user_by_string_id_and_token_null(self, url=config.get("url")):
        a = self.auth()
        r = requests.post(url + "/user/id", json={"token": " ",
                                                  "id": a.json()['result']['id']})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r)

    # def test_get_user_by_null_id_and_correct_token(self, url=config.get("url")):
    #     a = self.auth()
    #     r = requests.post(url + "/user/id", json={"token": a.json()['result']['token'],
    #                                               "id": 0})
    #     assert r.status_code == 401
    #     print(r)

    def test_get_regions_by_token(self, url=config.get("url")):
        a = self.auth()
        r = requests.post(url + "/user/regions", json={"token": a.json()["result"]["token"]})
        AssertThat(r.status_code).IsEqualTo(200)
        print(r.json())
        print(r)

    def test_get_regions_by_incorrect_token(self, url=config.get("url")):
        r = requests.post(url + "/user/regions", json={"token": "3AED6F4648F581DGVZEF6645C833DEFFC9B"})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r)

    def test_get_regions_by_token_null(self, url=config.get("url")):
        r = requests.post(url + "/user/regions", json={"token": ""})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r)

    def test_get_workgroup_by_token_and_region(self, url=config.get("url")):
        a = self.auth()
        r = requests.post(url + "/region/workgroup", json={"token": a.json()["result"]["token"],
                                                           "region": self.get_region_lam()})
        AssertThat(r.status_code).IsEqualTo(200)
        print(r.json())
        print(r)

    def test_get_workgroup_by_incorrect_token_and_correct_region(self, url=config.get("url")):
        r = requests.post(url + "/region/workgroup", json={"token": "3AED6F4648F581DGVZEF6645C833DEFFC9BAAVGBBGY",
                                                           "region": self.get_region_lam()})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())
        print(r)

    def test_get_workgroup_by_empty_token_and_correct_region(self, url=config.get("url")):
        r = requests.post(url + "/region/workgroup", json={"token": "                         ",
                                                           "region": self.get_region_lam()})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())
        print(r)

    def test_get_workgroup_by_incorrect_token_and_incorrect_region(self, url=config.get("url")):
        r = requests.post(url + "/region/workgroup", json={"token": "3AED6F4648F581DGVZEF6645C833DEFFC9BAAVGBBGY",
                                                           "region": self.random_value()})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r.json())
        print(r)

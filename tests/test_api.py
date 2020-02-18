import pytest
import requests
from truth.truth import AssertThat
from support import config


class TestApi:

    def auth(self, login=config.get("login"), password=config.get("password"), url=config.get("url")):
        body = {"login": login,
                "password": password}
        r = requests.post(url+"/login", headers={"Content-Type": "application/json"},
                          json=body)
        print(r.json())
        return r

    def test_validate_with_token(self, url=config.get("url")):
        r = self.auth()
        r = requests.post(url+"/user", json={'token': r.json()['result']['token']})
        AssertThat(r.json()['result']).ContainsItem("roles", ["ROLE_ABM_ADMIN"])
        print(r)

    def test_correct_login_with_data(self):
        r = self.auth()
        assert r.status_code == 200
        AssertThat(r.json()['result']).ContainsItem("roles", ["ROLE_ABM_ADMIN"])

    def test_incorrect_login_with_null(self):
        d = {"login": " ",
             "password": " "}
        r = requests.post(config.get('url') + "/login", json=d)
        AssertThat(r.status_code).IsEqualTo(401)
        # assert r.status_code == 401
        print(r.status_code)

    def test_incorrect_login_with_data(self):
        d = {"login": "123",
             "password": "123"}
        r = requests.post(config.get("url") + "/login", json=d)
        assert r.status_code == 401
        print(r.status_code)

    def test_get_user_with_incorrect_token(self):
        d = {"token": "3AED6F4648F581DEF6645C833DEFFC9B"}
        r = requests.post(config.get("url") + "/user", json=d)
        assert r.status_code == 401

    def test_get_user_with_token_null(self):
        d = {"token": " "}
        r = requests.post(config.get("url") + "/user", json=d)
        assert r.status_code == 401

    def test_get_user_by_string_id(self, username=config.get("login"), url=config.get("url")):
        r = self.auth()
        r = requests.post(url + "/user/username", json={"token": r.json()["result"]["token"],
                                                        "username": username})
        print(r)

    def test_get_user_by_string_id_incorrect_user(self, url=config.get("url")):
        v = self.auth()
        r = requests.post(url + "/user/username", json={"token": v.json()["result"]["token"],
                                                        "username": "123"})
        assert r.status_code == 401
        print(r.json())

    def test_get_user_by_string_id_incorrect_token(self, url=config.get("url")):
        r = requests.post(url + "/user/username", json={"token": " %%%%%%%",
                                                        "username": config.get("login")})
        assert r.status_code == 401
        print(r.json())

    def test_get_user_by_string_id_with_null(self, url=config.get("url")):
        r = requests.post(url + "/user/username", json={"token": "  ",
                                                        "username": "  "})
        assert r.status_code == 401
        print(r.json())

    def test_get_user_by_string_id_and_token(self, url=config.get("url")):
        a = self.auth()
        r = requests.post(url + "/user/id", json={"token": a.json()['result']['token'],
                                                  "id": a.json()['result']['id']})
        assert r.status_code == 200
        if 'roles' in r.json() and r.json()["result"]["roles"] != '5OLE_ABM_ADMIN':
            AssertionError and print("User with ID", a.json()['result']['id'], "is have not admin role")
        print(r)

    def test_get_user_by_string_id_and_incorrect_token_max_int(self, url=config.get("url")):
        a = self.auth()
        r = requests.post(url + "/user/id", json={"token": a.json()['result']['token'],
                                                  "id": 19223372036854775807})
        assert r.status_code == 401
        print(r.json())

    def test_get_user_by_string_id_and_token_null(self, url=config.get("url")):
        a = self.auth()
        r = requests.post(url + "/user/id", json={"token": " ",
                                                  "id": a.json()['result']['id']})
        assert r.status_code == 401
        print(r)

    def test_get_user_by_null_id_and_correct_token(self, url=config.get("url")):
        a = self.auth()
        r = requests.post(url + "/user/id", json={"token": a.json()['result']['token'],
                                                  "id": -0})
        assert r.status_code == 401
        print(r)



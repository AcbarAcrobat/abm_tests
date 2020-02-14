import requests
from truth.truth import AssertThat
from support import config


class TestApi:

    def auth(self, login=config.get("login"), password=config.get("password"), url=config.get("url")):
        body = {"login": login,
                "password": password}
        r = requests.post(url+"/login", headers={"Content-Type": "application/json"},
                          json=body)
        return r

    def test_validate_with_token(self, url=config.get("url")):
        r = self.auth()
        r = requests.post(url+"/user", json={'token': r.json()['result']['token']})
        AssertThat(r.json()['result']).ContainsItem("id", 3562)
        print(r)

    def test_correct_login_with_data(self):
        r = self.auth()
        assert r.status_code == 200
        AssertThat(r.json()['result']).ContainsItem("id", 3562)

    def test_incorrect_login_with_null(self):
        d = {"login": " ",
             "password": " "}
        r = requests.post(config.get('url') + "/login", json=d)
        assert r.status_code == 401
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
        v = self.auth()
        r = requests.post(url + "/user/username", json={"token": v.json()["result"]["token"],
                                                        "username": username})
        print(r)


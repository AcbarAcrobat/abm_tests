import requests

url = "http://192.168.0.125/netrisuser_api"


class SessionHelper:

    def login_with_data(self):
        d = {"login": "test_ABM_admin",
             "password": "test_ABM_admin"}
        r = requests.post(url + "/login", json=d)
        assert r.status_code == 200


login = SessionHelper()
login.login_with_data()
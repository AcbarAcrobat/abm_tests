import requests

url = "http://192.168.0.125/netrisuser_api"


class Tests:

    def incorrect_login(self):
        d = {"login": "123",
             "password": "123"}
        r = requests.post(url + "/login", json=d)
        assert r.status_code == 401
        print(r.status_code)


login = Tests()
login.incorrect_login()


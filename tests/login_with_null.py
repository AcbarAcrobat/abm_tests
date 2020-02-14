# import requests
#
# url = "http://192.168.0.125/netrisuser_api"
#
#
# class Tests:
#
#     def login_with_null(self):
#         d = {"login": " ",
#              "password": " "}
#         r = requests.post(url + "/login", json=d)
#         assert r.status_code == 401
#         print(r.status_code)
#
#
# login = Tests()
# login.login_with_null()

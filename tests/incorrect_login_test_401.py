# import requests
# import json
# from urllib.parse import urljoin
# from truth.truth import AssertThat
# url = "http://192.168.0.125/netrisuser_api"
#
#
# class IncorrectTest:
#
#     def incorrect_login(self):
#         d = {"login": "123",
#              "password": "123"}
#         r = requests.post(url + "/login", json=d)
#         assert r.status_code == 401
#         print(r.status_code)
#
#
# login = IncorrectTest()
# login.incorrect_login()
#

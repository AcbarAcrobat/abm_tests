# import requests
# import json
# from urllib.parse import urljoin
# from truth.truth import AssertThat
# from support import config
#
#
# class CorrectLoginTest:
#
#     def auth(self, login, password):
#         config.get('login')
#         config.get('password')
#         body = {
#             "login": config.get('login'),
#             "password": config.get('password')
#         }
#         r = requests.post(
#             urljoin(config.get('url'), "/login"),
#             json=body
#         )
#         return r
#
#     def test_login_with_data(self):
#         r = self.auth(config.get('login'), config.get('password'))
#         token, user_id = r.json()['result']['token'], r.json()['result']['id']
#
#         assert r.status_code == 200
#         AssertThat(r.json()['result']).ContainsItem(user_id, 3562)
#
#
# login = CorrectLoginTest()
# login.test_login_with_data()

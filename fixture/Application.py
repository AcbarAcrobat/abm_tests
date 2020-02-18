import requests

from fixture.Session import SessionHelper
from support import config


class Application:

    def __init__(self):
        """These are launch artifacts"""
        self.session = SessionHelper(self)

    # def auth(self, login=config.get("login"), password=config.get("password"), url=config.get("url")):
    #     body = {"login": login,
    #             "password": password}
    #     r = requests.post(url + "/login", headers={"Content-Type": "application/json"},
    #                       json=body)
    #     return r

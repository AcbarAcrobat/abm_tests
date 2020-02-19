from support import config


class TestData:

    def url(self):
        url = config.get("url")
        return url

    def username(self):
        login = config.get("login")
        return login

    def password(self):
        password = config.get("password")
        return password

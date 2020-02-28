from support import config


class TestData:

    def url(self):
        return config.get("url")

    def username(self):
        return config.get("login")

    def password(self):
        return config.get("password")

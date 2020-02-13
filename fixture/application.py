import logging
from fixture.session import SessionHelper

url = "http://192.168.0.125/netrisuser_api"


class Application:
    LOGGER = logging.getLogger(__name__)

    def __init__(self):
        """These are launch artifacts"""
        self.session = SessionHelper(self)



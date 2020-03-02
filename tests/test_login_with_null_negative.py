import allure
import requests
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper
import logging


LOGGER = logging.getLogger(__name__)
T = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/login")
@allure.title("Post login with incorrect values")
def test_incorrect_login_with_null():
    with allure.step("Send request to the server with empty token and password"):
        r = requests.post(T.url() + "/login", json={"login": "   ",
                                                    "password": "   "})
    with allure.step("LOGGER response"):
        LOGGER.info(r.status_code)
        LOGGER.info(r.json())
    with allure.step("Assert status code is 401"):
        AssertThat(r.status_code).IsEqualTo(401)

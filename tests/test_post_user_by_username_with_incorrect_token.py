import allure
import requests
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper
from data_generator.password_generator import random_password
import logging


LOGGER = logging.getLogger(__name__)
T = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/user/username")
@allure.title("Post request with incorrect values")
def test_post_user_by_username_with_incorrect_token():
    with allure.step("Send request to the server with correct username and incorrect token"):
        r = requests.post(T.url() + "/user/username", json={"token": random_password(),
                                                            "username": T.username()})
    with allure.step("LOGGER response"):
        LOGGER.info(r.status_code)
        LOGGER.info(r.json())
    with allure.step("Assert status code is 401"):
        AssertThat(r.status_code).IsEqualTo(401)


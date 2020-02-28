import allure
import requests
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper
from generator.password_generator import random_password
import logging

LOGGER = logging.getLogger(__name__)
T = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/user")
@allure.title("Post request with incorrect token")
def test_post_user_with_incorrect_token():
    with allure.step("Send request to the server with incorrect token={random_password()}"):
        r = requests.post(T.url() + "/user", json={"token": random_password()})
    with allure.step("Assert status code 401 in server response"):
        AssertThat(r.status_code).IsEqualTo(401)
    with allure.step("LOGGER response"):
        LOGGER.info(r.status_code)
        LOGGER.info(r.json())

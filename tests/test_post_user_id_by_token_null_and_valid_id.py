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
@allure.sub_suite("/user/id")
@allure.title("Post request with incorrect values")
def test_post_user_by_string_id_and_token_null():
    with allure.step('Send request to the server with empty token and correct id'):
        r = requests.post(T.url() + "/user/id", json={"token": " ",
                                                      "id": H.get_id()})
    with allure.step("Assert status code is 401"):
        AssertThat(r.status_code).IsEqualTo(401)
    with allure.step("LOGGER response"):
        LOGGER.info(r.status_code)
        LOGGER.info(r.json())

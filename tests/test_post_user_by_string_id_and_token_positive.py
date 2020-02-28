import allure
import requests
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper
import logging

LOGGER = logging.getLogger(__name__)
T = TestData()
H = Helper()


@allure.parent_suite("POSITIVE")
@allure.sub_suite("/user/id")
@allure.title("Post request with correct values")
def test_post_user_by_id_and_token_positive():
    with allure.step("Send request to the server with correct token and id"):
        r = requests.post(T.url() + "/user/id", json={"token": H.tok3n(),
                                                      "id": H.get_id()})
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    with allure.step("Assert contains result in r.json()"):
        AssertThat(r.json()).ContainsKey("result")
    with allure.step("LOGGER response"):
        LOGGER.info(r.status_code)
        LOGGER.info(r.json())

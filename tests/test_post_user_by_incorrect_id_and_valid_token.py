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
def test_post_user_by_id_and_correct_token_max_int():
    with allure.step("Send request to the server with correct token and incorrect id"):
        r = requests.post(T.url() + "/user/id", json={"token": H.tok3n(),
                                                      "id": 9223372036854775807})
    with allure.step("Assert status code is 400"):
        AssertThat(r.status_code).IsEqualTo(400)
    with allure.step("LOGGER response"):
        LOGGER.info(r.status_code)
        LOGGER.info(r.json())

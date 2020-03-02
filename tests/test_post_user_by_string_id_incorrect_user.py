import allure
import requests
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper
import logging


LOGGER = logging.getLogger(__name__)
TeD = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/user/username")
@allure.title("Post request with incorrect values")
def test_post_user_by_string_id_incorrect_user():
    with allure.step("Send request to the server with correct token and incorrect username"):
        r = requests.post(TeD.url() + "/user/username", json={"token": H.tok3n(),
                                                              "username": H.random_value()})
    with allure.step("LOGGER response"):
        LOGGER.info(r.status_code)
        LOGGER.info(r.json())
    with allure.step("Assert status code is"):
        AssertThat(r.status_code).IsEqualTo(401)


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
@allure.sub_suite("/user/username")
@allure.title("Post request to the url + /user/username")
def test_post_user_by_username_and_token():
    with allure.step("Send request to the server"):
        r = requests.post(T.url() + "/user/username", json={"token": H.tok3n(),
                                                            "username": T.username()})
    with allure.step("Assert 200 status code"):
        AssertThat(r.status_code).IsEqualTo(200)
    with allure.step("Assert contains result in r.json()"):
        AssertThat(r.json()).ContainsKey("result")
    with allure.step("LOGGER response"):
        LOGGER.info(r.status_code)
        LOGGER.info(r.json())

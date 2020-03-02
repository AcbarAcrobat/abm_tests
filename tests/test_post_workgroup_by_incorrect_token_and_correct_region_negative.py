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
@allure.sub_suite("/region/workgroup")
@allure.title("Post request with incorrect values")
def test_get_workgroup_by_incorrect_token_and_correct_region():
    with allure.step("Send request to the server with incorrect token and correct region value"):
        r = requests.post(T.url() + "/region/workgroup", json={"token": random_password(),
                                                               "region": H.get_user_regions()})
    with allure.step("LOGGER response"):
        LOGGER.info(r.status_code)
        LOGGER.info(r.json())
    with allure.step("Assert status code is 401"):
        AssertThat(r.status_code).IsEqualTo(401)


import allure
import requests
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper
from generator.password_generator import randomPassword

TeD = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/login")
@allure.title("Post login with incorrect values")
def test_incorrect_login_with_null():
    with allure.step("Send request to the server with empty token and password"):
        r = requests.post(TeD.url() + "/login", json={"login": "   ",
                                                      "password": "   "})
    with allure.step("Assert status code is 401"):
        AssertThat(r.status_code).IsEqualTo(401)
    print(r.status_code)

import allure
import requests
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper
from generator.password_generator import randomPassword

TeD = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/user")
@allure.title("Post request with incorrect token")
def test_post_user_with_incorrect_token():
    with allure.step("Send request to the server with incorrect token={randomPassword()}"):
        r = requests.post(TeD.url() + "/user", json={"token": randomPassword()})
    with allure.step("Assert status code 401 in server response"):
        AssertThat(r.status_code).IsEqualTo(401)
    print(r.status_code)

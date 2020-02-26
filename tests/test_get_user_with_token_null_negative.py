import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper
from generator.password_generator import randomPassword

TeD = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/user")
@allure.title("Post user with incorrect token")
def test_post_user_with_token_null():
    with allure.step("Send request to the server with token null"):
        r = requests.post(TeD.url() + "/user", json={"token": " "})
    with allure.step("Assert status code is 401"):
        AssertThat(r.status_code).IsEqualTo(401)
    print(r.status_code)

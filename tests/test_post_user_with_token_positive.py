import allure
import requests
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper


T = TestData()
H = Helper()


@allure.parent_suite("POSITIVE")
@allure.sub_suite("/user")
@allure.title("Post request to the server")
def test_post_user_with_token():
    with allure.step("Send request to the server with valid token"):
        r = requests.post(T.url() + "/user", json={'token': H.tok3n()})
    with allure.step("Assert 200 status code"):
        AssertThat(r.status_code).IsEqualTo(200)
    with allure.step("Assert contains result in r.json()"):
        AssertThat(r.json()).ContainsKey("result")
    with allure.step("Assert ROLE_ABM_ADMIN and ROLE_MAIN_OPERATOR in r.json()[result]"):
        AssertThat(r.json()["result"]["roles"])\
            .ContainsAllIn(['ROLE_ABM_ADMIN', 'ROLE_MAIN_OPERATOR'])
    print(r.status_code)
    print(r.json())

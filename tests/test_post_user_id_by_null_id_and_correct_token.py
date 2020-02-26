import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper
from generator.password_generator import randomPassword

T = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/user/id")
@allure.title("Post request with incorrect values")
def test_get_user_by_null_id_and_correct_token():
    with allure.step("Send request to the server with correct token and id 0"):
        r = requests.post(T.url() + "/user/id", json={"token": H.tok3n(),
                                                      "id": 0})
    with allure.step("Assert status code is 401"):
        AssertThat(r.status_code).IsEqualTo(401)
    print(r)

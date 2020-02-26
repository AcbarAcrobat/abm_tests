import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper

T = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/user/id")
@allure.title("Post request with incorrect values")
def test_post_user_by_id_and_correct_token_max_int():
    with allure.step("Send request to the server with correct token and incorrect id"):
        r = requests.post(T.url() + "/user/id", json={"token": H.tok3n(),
                                                      "id": 9223372036854775807})
    with allure.step("Assert status code is 401"):
        AssertThat(r.status_code).IsEqualTo(401)
    print(r.json())

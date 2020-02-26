import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper

T = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/user/regions")
@allure.title("Post request with incorrect values")
def test_get_workgroup_by_empty_token_and_correct_region():
    with allure.step("Send request to the server with correct region and empty token"):
        r = requests.post(T.url() + "/region/workgroup", json={"token": "                         ",
                                                               "region": H.get_user_regions()})
    with allure.step("Assert status code is 401"):
        AssertThat(r.status_code).IsEqualTo(401)
    print(r.json())
    print(r)

import allure
import requests
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper

T = TestData()
H = Helper()


@allure.parent_suite("POSITIVE")
@allure.sub_suite("/region/workgroup")
@allure.title("Post request with correct values")
def test_get_workgroup_by_token_and_region():
    with allure.step("Send request to the server with correct token and region number"):
        r = requests.post(T.url() + "/region/workgroup", json={"token": H.tok3n(),
                                                               "region": H.get_user_regions()})
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())
    print(r)

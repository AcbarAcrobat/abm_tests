import allure
import requests
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper

T = TestData()
H = Helper()


@allure.parent_suite("POSITIVE")
@allure.sub_suite("/user/regions")
@allure.title("Post request with correct values")
def test_get_regions_by_token():
    with allure.step("Send request to the server with correct token"):
        r = requests.post(T.url() + "/user/regions", json={"token": H.tok3n()})
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())
    print(r)

import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper
from generator.password_generator import randomPassword

T = TestData()
H = Helper()


@allure.parent_suite("NEGATIVE")
@allure.sub_suite("/user/regions")
@allure.title("Post request with incorrect token")
def test_get_regions_by_incorrect_token():
    with allure.step("Send request to the server with randomize token"):
        r = requests.post(T.url() + "/user/regions", json={"token": randomPassword()})
    with allure.step("Assert status code is 401"):
        AssertThat(r.status_code).IsEqualTo(401)
    print(r)

import allure
from truth.truth import AssertThat
from utils.testdata import TestData
from utils.helper import Helper


TeD = TestData()
H = Helper()


@allure.parent_suite("POSITIVE")
@allure.sub_suite("/login")
@allure.title("Post login with correct values")
def test_correct_login_with_data():
    with allure.step('send request to the server with {r}'):
        r = H.autorize()
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())

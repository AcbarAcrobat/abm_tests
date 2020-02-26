import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper
from generator.password_generator import randomPassword

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

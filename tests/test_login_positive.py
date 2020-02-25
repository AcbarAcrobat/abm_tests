import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper
from generator.password_generator import randomPassword

TeD = TestData()
H = Helper()


@allure.step('step2')
def test_correct_login_with_data(self):
    with allure.step('send request to the server with {r}'):
        r = H.autorize()
        AssertThat(r.status_code).IsEqualTo(200)
        # AssertThat(r.json()['result']).ContainsItem("roles", ["ROLE_ABM_ADMIN"])
        print(r.json())
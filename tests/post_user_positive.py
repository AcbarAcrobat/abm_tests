import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper

TeD = TestData()
H = Helper()


@allure.step('step1')
def test_post_user_with_token(self):
    with allure.step('send request to the server with token = {H.tok3n}'):
        r = requests.post(TeD.url() + "/user", json={'token': H.tok3n()})
        AssertThat(r.status_code).IsEqualTo(200)
        AssertThat(r.json()['result']).ContainsItem("roles", ["ROLE_ABM_ADMIN", "ROLE_MAIN_OPERATOR"])
        print(r.status_code)
        print(r.json())
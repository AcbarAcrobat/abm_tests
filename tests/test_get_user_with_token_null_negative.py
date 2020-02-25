import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper
from generator.password_generator import randomPassword

TeD = TestData()
H = Helper()


def test_get_user_with_token_null(self):
    r = requests.post(TeD.url() + "/user", json={"token": " "})
    AssertThat(r.status_code).IsEqualTo(401)
    print(r.status_code)

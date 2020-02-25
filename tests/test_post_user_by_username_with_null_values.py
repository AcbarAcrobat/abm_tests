import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper
from generator.password_generator import randomPassword

T = TestData()
H = Helper()


def test_get_user_by_string_id_with_null(self):
    r = requests.post(T.url() + "/user/username", json={"token": "  ",
                                                        "username": "  "})
    AssertThat(r.status_code).IsEqualTo(401)
    print(r.json())
    print(r.status_code)

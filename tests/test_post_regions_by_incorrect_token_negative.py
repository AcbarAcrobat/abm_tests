import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper
from generator.password_generator import randomPassword

T = TestData()
H = Helper()


def test_get_regions_by_incorrect_token():
    r = requests.post(T.url() + "/user/regions", json={"token": randomPassword()})
    AssertThat(r.status_code).IsEqualTo(401)
    print(r)

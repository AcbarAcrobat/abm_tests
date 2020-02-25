import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper

T = TestData()
H = Helper()


def test_get_regions_by_token_null():
    r = requests.post(T.url() + "/user/regions", json={"token": "   "})
    AssertThat(r.status_code).IsEqualTo(401)
    print(r)

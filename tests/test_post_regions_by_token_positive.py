import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper

T = TestData()
H = Helper()


def test_get_regions_by_token():
    r = requests.post(T.url() + "/user/regions", json={"token": H.tok3n()})
    AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())
    print(r)

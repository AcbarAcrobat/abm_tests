import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper

T = TestData()
H = Helper()


def test_get_workgroup_by_token_and_region(self):
    r = requests.post(T.url() + "/region/workgroup", json={"token": H.tok3n(),
                                                           "region": H.get_user_regions()})
    AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())
    print(r)

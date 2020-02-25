import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper
from generator.password_generator import randomPassword

T = TestData()
H = Helper()


def test_get_workgroup_by_incorrect_token_and_incorrect_region(self):
    r = requests.post(T.url() + "/region/workgroup", json={"token": randomPassword(),
                                                           "region": H.get_user_regions()})
    AssertThat(r.status_code).IsEqualTo(401)
    print(r.json())
    print(r)

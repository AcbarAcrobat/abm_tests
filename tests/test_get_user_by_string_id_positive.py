import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper

T = TestData()
H = Helper()


@allure.step("Post url + /user/username with token={'H.tok3n()'} and username={'T.username()'}")
def test_get_user_by_string_id():
    with allure.step("send request to the server with values token={'H.tok3n()'} and username={'T.username()"):
        r = requests.post(T.url() + "/user/username", json={"token": H.tok3n(),
                                                            "username": T.username()})
        AssertThat(r.status_code).IsEqualTo(200)
        print(r.status_code)

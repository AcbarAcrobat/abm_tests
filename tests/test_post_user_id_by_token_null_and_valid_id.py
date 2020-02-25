import allure
import requests
from truth.truth import AssertThat
from src.testdata import TestData
from src.helper import Helper

T = TestData()
H = Helper()


@allure.step('Post url + /user/id with empty token and id={"H.get_id()"}')
def test_post_user_by_string_id_and_token_null():
    with allure.step('Send request to the server'):
        r = requests.post(T.url() + "/user/id", json={"token": " ",
                                                      "id": H.get_id()})
        AssertThat(r.status_code).IsEqualTo(401)
        print(r)

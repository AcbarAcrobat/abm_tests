# import allure
# import requests
# from truth.truth import AssertThat
# from src.testdata import TestData
# from src.helper import Helper
# from generator.password_generator import randomPassword
#
# T = TestData()
# H = Helper()
#
#
# def test_get_user_by_null_id_and_correct_token():
#         a = H.autorize()
#         r = requests.post(TeD.url() + "/user/id", json={"token": a.json()['result']['tok3n'],
#                                                         "id": 0})
#         AssertThat(r.status_code).IsEqualTo(401)
#         print(r)
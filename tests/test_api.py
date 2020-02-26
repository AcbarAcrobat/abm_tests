# import allure
# import requests
# from truth.truth import AssertThat
# from src.testdata import TestData
# from src.helper import Helper
# from generator.password_generator import randomPassword
#
# T = TestData()
# H = Helper()


# class TestApi:

    # @allure.step('step1')
    # def test_post_user_with_token(self):
    #     with allure.step('send request to the server with token = {H.tok3n}'):
    #         r = requests.post(TeD.url() + "/user", json={'token': H.tok3n()})
    #         AssertThat(r.status_code).IsEqualTo(200)
    #         AssertThat(r.json()['result']).ContainsItem("roles", ["ROLE_ABM_ADMIN", "ROLE_MAIN_OPERATOR"])
    #         print(r.status_code)
    #         print(r.json())

    # @allure.step('step2')
    # def test_correct_login_with_data(self):
    #     with allure.step('send request to the server with {r}'):
    #         r = H.autorize()
    #         AssertThat(r.status_code).IsEqualTo(200)
    #         # AssertThat(r.json()['result']).ContainsItem("roles", ["ROLE_ABM_ADMIN"])
    #         print(r.json())

    # def test_incorrect_login_with_null(self):
    #     r = requests.post(TeD.url() + "/login", json={"login": "   ",
    #                                                   "password": "   "})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.status_code)

    # def test_incorrect_login_with_data(self):
    #     r = requests.post(TeD.url() + "/login", json={"login": randomPassword(),
    #                                                   "password": randomPassword()})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.status_code)

    # def test_post_user_with_incorrect_token(self):
    #     r = requests.post(TeD.url() + "/user", json={"token": randomPassword()})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.status_code)

    # def test_post_user_with_token_null(self):
    #     r = requests.post(TeD.url() + "/user", json={"token": " "})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.status_code)

    # def test_post_user_by_username_and_token(self):
    #     r = requests.post(TeD.url() + "/user/username", json={"token": H.tok3n(),
    #                                                           "username": TeD.username()})
    #     print(r.status_code)

    # def test_get_user_by_string_id_incorrect_user(self):
    #     r = requests.post(TeD.url() + "/user/username", json={"token": H.tok3n(),
    #                                                           "username": H.random_value()})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.json())
    #     print(r.status_code)

    # def test_get_user_by_string_id_incorrect_token(self):
    #     r = requests.post(TeD.url() + "/user/username", json={"token": randomPassword(),
    #                                                           "username": TeD.username()})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.json())
    #     print(r.status_code)

    # def test_get_user_by_string_id_with_null(self):
    #     r = requests.post(T.url() + "/user/username", json={"token": "  ",
    #                                                           "username": "  "})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.json())
    #     print(r.status_code)

    # def test_post_user_by_id_and_token_positive(self):
    #     r = requests.post(T.url() + "/user/id", json={"token": H.tok3n(),
    #                                                     "id": H.get_id()})
    #     AssertThat(r.status_code).IsEqualTo(200)
    #     if 'roles' in r.json() and r.json()["result"]["roles"] != ["5OLE_ABM_ADMIN"]:
    #         AssertionError and print("User with ID", r.json()['result']['id'], "is have not admin role")
    #     print(r.status_code)

    # def test_post_user_by_id_and_correct_token_max_int(self):
    #     a = H.autorize()
    #     r = requests.post(TeD.url() + "/user/id", json={"token": a.json()['result']['tok3n'],
    #                                                     "id": 9223372036854775807})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.json())

    # def test_get_user_by_string_id_and_token_null(self):
    #     r = requests.post(T.url() + "/user/id", json={"token": " ",
    #                                                     "id": H.get_id()})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r)

    # def test_get_user_by_null_id_and_correct_token(self):
    #     a = H.autorize()
    #     r = requests.post(TeD.url() + "/user/id", json={"token": a.json()['result']['tok3n'],
    #                                                     "id": 0})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r)

    # def test_get_regions_by_token(self):
    #     r = requests.post(T.url() + "/user/regions", json={"token": H.tok3n()})
    #     AssertThat(r.status_code).IsEqualTo(200)
    #     print(r.json())
    #     print(r)

    # def test_get_regions_by_incorrect_token(self):
    #     r = requests.post(T.url() + "/user/regions", json={"token": randomPassword()})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r)

    # def test_get_regions_by_token_null(self):
    #     r = requests.post(T.url() + "/user/regions", json={"token": "   "})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r)

    # def test_get_workgroup_by_token_and_region(self):
    #     r = requests.post(T.url() + "/region/workgroup", json={"token": H.tok3n(),
    #                                                              "region": H.get_user_regions()})
    #     AssertThat(r.status_code).IsEqualTo(200)
    #     print(r.json())
    #     print(r)

    # def test_get_workgroup_by_incorrect_token_and_correct_region(self):
    #     r = requests.post(T.url() + "/region/workgroup", json={"token": randomPassword(),
    #                                                              "region": H.get_user_regions()})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.json())
    #     print(r)

    # def test_get_workgroup_by_empty_token_and_correct_region(self):
    #     r = requests.post(T.url() + "/region/workgroup", json={"token": "                         ",
    #                                                              "region": H.get_user_regions()})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.json())
    #     print(r)

    # def test_get_workgroup_by_incorrect_token_and_incorrect_region(self):
    #     r = requests.post(T.url() + "/region/workgroup", json={"token": randomPassword(),
    #                                                              "region": H.get_user_regions()})
    #     AssertThat(r.status_code).IsEqualTo(401)
    #     print(r.json())
    #     print(r)

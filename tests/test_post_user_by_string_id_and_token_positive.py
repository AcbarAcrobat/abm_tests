def test_get_user_by_string_id_and_token(self):
    r = requests.post(T.url() + "/user/id", json={"token": H.tok3n(),
                                                  "id": H.get_id()})
    AssertThat(r.status_code).IsEqualTo(200)
    if 'roles' in r.json() and r.json()["result"]["roles"] != ["5OLE_ABM_ADMIN"]:
        AssertionError and print("User with ID", r.json()['result']['id'], "is have not admin role")
    print(r.status_code)
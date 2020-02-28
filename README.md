# abm_tests

Preparatory Activities:
```
$ sudo apt install python3.8
$ sudo apt install python3-pip
```

After that go to /dir/dir/abm_tests and create virtualenv
```
$ sudo python3 -m venv venv
$ source venv/bin/activate
```
Then install required packages with pip
```
$ pip install -r requirements.txt
```
And run the tests
```
$ pytest -sv --alluredir=allure_results tests/
```

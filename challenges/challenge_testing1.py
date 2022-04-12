import cat_challenge

import requests

URL = 'https://cat-fact.herokuapp.com/facts'

def test_get_cat_fact_check_status_code_equals_200():
    response = requests.get(URL)
    assert response.status_code == 200

def test_get_cat_fact_check_content_type_equals_json():
     response = requests.get(URL)
     assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

def test_get_cat_fact_check_content_list_size_equals_5():
    response = requests.get(URL)
    assert len(response.json()) == 5


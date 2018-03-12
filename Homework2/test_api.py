import requests
import json

def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_api1__basic():
    response = requests.get("https://datausa.io/about/api/")
    assert response
    assert response.status_code == 200
    print (response.status_code)
    print(response.headers)
    assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'
    print(response.headers['Content-Type'])
    
def test_api2__basic():
    payload = {'show': 'geo', 'sumlevel': 'nation', 'year': 'latest', 'required': 'pop' }
    response = requests.get("https://api.datausa.io/api", params=payload)
    assert response
    assert response.status_code == 200
    print (response.status_code)
    print(response.headers)
    assert response.headers['Content-Type'] == 'application/json'
    print(response.headers['Content-Type'])
    result = json.loads(response.text)
    assert type(result) is dict
    print (type(result))
    print (result)
    assert len(result) == 5
    print (len(result))    
    
    
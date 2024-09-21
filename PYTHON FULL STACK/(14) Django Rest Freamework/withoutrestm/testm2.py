import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def get_resource(id = None):
    data = {}
    if id is not None:
        data={
            'id':id
        }
    resp = requests.get(BASE_URL+ENDPOINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

# id = input('Enter Employee ID: ')
get_resource()

def create_resource():
    new_emp = {
        "eno": 110000,
        "ename": "aki",
        "esal": 90000,
        "eaddr": "china"      
    }
    resp = requests.post(BASE_URL+ ENDPOINT, data=json.dumps(new_emp))  #while posting data it is necessary to post it in json format 
    print(resp.status_code)
    print(resp.json())

# create_resource()

def update_resource(id):
    new_emp = {
        "id": id,
        "eno": 1000,
        "esal": 10000,
        "eaddr": "korea"      
    }
    resp = requests.put(BASE_URL+ ENDPOINT, data=json.dumps(new_emp))  #while posting data it is necessary to post it in json format 
    print(resp.status_code)
    print(resp.json())

# update_resource(10)

def delete_resource(id):
    data={
            'id':id
    }
    resp = requests.delete(BASE_URL+ ENDPOINT, data=json.dumps(data))      
    print(resp.status_code)
    print(resp.json())   

# delete_resource(11)
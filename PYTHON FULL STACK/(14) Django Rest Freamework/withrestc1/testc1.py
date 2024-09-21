import time
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
get_resource(2)

# time.sleep(20)
# print('post request...')

def create_resource():
    new_emp = {
        "eno": 600,
        "ename": "sasaki",
        "esal": 6000,
        "eaddr": "japan"      
    }
    resp = requests.post(BASE_URL+ ENDPOINT, data=json.dumps(new_emp))  #while posting data it is necessary to post it in json format 
    print(resp.status_code)
    print(resp.json())

# create_resource()

# time.sleep(20)
# print('create request...')

def update_resource(id):
    new_emp = {
        "id": id,
        # "ename": "SUNNY",         # uncomment to check object klevel validation
        "esal": 4000,
        "eaddr": "dehli"      
    }
    resp = requests.put(BASE_URL+ ENDPOINT, data=json.dumps(new_emp))  # while posting data it is necessary to post it in json format 
    print(resp.status_code)
    print(resp.json())

# update_resource(4)

# time.sleep(20)
# print('delete request...')

def delete_resource(id):
    data={
            'id':id
    }
    resp = requests.delete(BASE_URL+ ENDPOINT, data=json.dumps(data))      
    print(resp.status_code)
    print(resp.json())   

# delete_resource(6)
import json
import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
def get_resource(id):
    resp = requests.get(BASE_URL+ ENDPOINT + id +'/')      
    print(resp.status_code)
    print(resp.json())   

    # # if any error occur while retriving data then to handle it...this is best as partner application deeveloper but if youre django api developer then try to handle it while creating api
    # if resp.status_code in range(200,300):
    # # if resp.status_code == requests.codes.ok:          # can use two if
    #     print(resp.json())
    # else:
    #     print('Something goes wrong')
"""
status code 
1XX --> informational
2XX --> successful 
3XX --> redirectional
4XX --> client error
5XX --> server error
"""
id = input('Enter Employee id: ')
get_resource(id)


def get_all():
    resp = requests.get(BASE_URL+ ENDPOINT)
    print(resp.status_code)
    print(resp.json())

get_all()

def create_resource():
    new_emp = {
        "eno": 800,
        "ename": "isaki",
        "esal": 80000,
        "eaddr": "china"      
    }
    resp = requests.post(BASE_URL+ ENDPOINT, data=json.dumps(new_emp))  #while posting data it is necessary to post it in json format 
    print(resp.status_code)
    print(resp.json())

# create_resource()

def update_resource(id):
    new_emp = {
        "esal": 8000,
        "eaddr": "japan"      
    }
    resp = requests.put(BASE_URL+ ENDPOINT + str(id) +'/', data=json.dumps(new_emp))  #while posting data it is necessary to post it in json format 
    print(resp.status_code)
    print(resp.json())

# update_resource(8)

def delete_resource(id):
    resp = requests.delete(BASE_URL+ ENDPOINT + str(id) +'/')      
    print(resp.status_code)
    print(resp.json())   

delete_resource(9)


def delete_resource(id):
    resp = requests.delete(BASE_URL+ ENDPOINT + str(id) +'/')      
    print(resp.status_code)
    print(resp.json())   

delete_resource(9)
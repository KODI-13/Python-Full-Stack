import requests
import json

BASE_url = 'http://127.0.0.1:8000/'
ENDPOINT = 'JSONResp/'

resp = requests.get(BASE_url + ENDPOINT)  # *NOTE = resp is httpresponse which is directly contain json thats why we can directly ask resp.json()
data = resp.json()   # it will automatically converted in dictionary by .json()
print("Data coming from function based view")
print(data)
print(type(data)) 
print("employee number: ",data['eno'])
print("employee name: ",data['ename']) 
print("employee salary: ",data['esal']) 
print("employee address: ",data['eaddr']) 
"""
===============
views.py notes
===============
"""
print('='*100, end='\n\n')
#testing class based view for get request
BASE_url = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijsonCBV/'

resp = requests.get(BASE_url + ENDPOINT)  
data = resp.json()   #  resp is httpresponse which is directly contain json thats why we can directly ask resp.json() ..it will automatically converted in dictionary by .json()
print("Data coming from class based view")
print(data)




print('='*100, end='\n\n')
#testing class based view for post request
BASE_url = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijsonCBV/'

resp = requests.post(BASE_url + ENDPOINT)  # *NOTE = it will genrate error beacuse we are posting data but not providing csrf token 
data = resp.json()   
print("Data coming from class based view")
print(data)

"""
csrf token is neccessary while posting the data 
middleware is responsible for csrf token verification
there are three ways to post data without passing csrf token or verification
1st way
        on the django application > settings> inside middleware > comment 'django.middleware.csrf.CsrfViewMiddleware'
        but this way is not allowed in productioin level
=============
views.py
=============

2nd way
"""


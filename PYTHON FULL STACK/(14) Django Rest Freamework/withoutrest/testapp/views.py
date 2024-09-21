from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# sending html response
def emp_data_view(request):
    emp_data={
        'eno':100,
        'ename': 'raj',
        'esal': 10000,
        'eaddr': 'pune'
    }
    resp = '<h1>employee number: {}<br> employee name: {}<br> employee salary: {}<br> employeeb address: {}<br></h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)   # *NOTE == as we are sending http response we can nuse html syntax in above string

"""
above html reasponse is only understandable by end user but other software application made of other languiages cant understand it
thats why we have to use json (javascript object notation) that can be undertandable by any softwere application in the world..

python contains inbuilt module that is json module
dumps() --> convert python dict to json object
loads() --> convert json data to python dict
"""

import json

#sending json rsponse 
#1st way
def emp_data_jsonview(request):
    emp_data={
        'eno':100,
        'ename': 'raj',
        'esal': 10000,
        'eaddr': 'pune'
    }
    json_data =  json.dumps(emp_data)
    return HttpResponse(json_data, content_type='application/json')    # if we didnt mention content_type then it ios going to consider it as HTML response


from django.http import JsonResponse
#2nd way
def emp_data_jsonview2(request):
    emp_data={
        'eno':100,
        'ename': 'raj',
        'esal': 10000,
        'eaddr': 'pune'
    }
    return JsonResponse(emp_data)  


"""
1) sending http request from browser
py manage.py runserver using these command we are sending http request from browser

2) sending http request from cmd line
also we can send http request from command prompt/line
command line http clients --> curl, httpie (pip install httpie) 
use in command line 
            'C:\\Users\\ritik>http http://127.0.0.1:8000/HTMLResp/'
            'C:\\Users\\ritik>http http://127.0.0.1:8000/JSONResp/'

3) sending http request from python file
in order send http request from python file we need a module named called as "Requests"
sfter that we can reciceve json response and we can convert it into dict and use it
==============
testapp notes
==============
"""


"""
continue from here
class based view --> every class based view is a child class of View
"""
from django.http import JsonResponse
from django.views.generic import View
from testapp.mixins import HttpResponseMixin

class JsonCBV(HttpResponseMixin, View):      #1st check url pattern for these and test it using test.py
    def get(self, request, *args, **kwargs):
        # emp_data={
        # 'eno':100,
        # 'ename': 'raj',
        # 'esal': 10000,
        # 'eaddr': 'pune'
        # }
        # return JsonResponse(emp_data)  
        json_data = json.dumps({'msg':'this is from get method'})
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs): #2nd test this using test.py and check notes related to post in test.py
        json_data = json.dumps({'msg':'this is from post method'})
        return self.render_to_http_response(json_data)
    
"""
mixin ==> means mixed in
          it is a parent class which ONLY used to provied functionality to the child class
          we does not create an object for it 
          mixin class is direct child class of object only  it wont extend with another parent class
          advantage -->
                        code reusability purpose

mixin used in above example

                    mixins                                                                multiple inheritance
parent class instantiation is not possible                                 parent class instantiation is possible(can create an object for parent class)
parent class contains only instance method not instance variable           parent class contains both instance method and instance variable          
these methods only useful for child class                                  these methods useful for both parent and child class
parent class should be direct child class of only object                   parent class can extended with anyother classes it does not need to be and object class
"""


# performing database crud operation without using REST Fraemework
# go to withoutrestm project
from django.shortcuts import render

# Create your views here.


"""
performing database crud operation without using REST Fraemework 

1. create model class
2. perform makemigrations and migrate
            makemigrations --> genrate bsql queries
            migrate -->< execute sql queies
3. register model in admin interface
4. create superuser  

added some data through admin section in employee in order to peerform operations

[A] Retriving data from database (required two classed based view)
        a) get a perticular record based on matched id
        b) get all records
"""
from django.views.generic import View
from testappm.models import Employee
import json                    #after use of SerializeMixin this is not used
from django.http import HttpResponse
from django.core.serializers import serialize      #after use of SerializeMixin this is not used
from testappm.mixins import SerializeMixin, HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testappm.utils import is_json
from testappm.forms import EmployeeForm

# a) get a perticular record based on matched id
@method_decorator(csrf_exempt, name='dispatch')
class EmplyeeDetailCBV(HttpResponseMixin, SerializeMixin, View):
    def get_object_by_id(self, id):
        try:
              emp = Employee.objects.get(id=id)       #employee Object data
        except Employee.DoesNotExist:
              emp = None
        return emp
        
    def get(self, request,  id, *args, **kwargs):    #1st run these using testappm.py 
        try:
              emp = Employee.objects.get(id=id)       #employee Object data
        # emp_data = {                            #converted into dictionary so we can dumps it into json and provied it to the partner application
        #     'eno': emp.eno,                       
        #     'ename': emp.ename,
        #     'esal': emp.esal,
        #     'eaddr': emp.eaddr              
        # }
        # json_data = json.dumps(emp_data)              # 1st uncomment upto above and try it

        # json_data = serialize('json', [emp,], fields = ('eno', 'ename', 'eaddr' ))    # django serialize function
        except Employee.DoesNotExist:
              json_data = json.dumps({'msg':'THe requested resource is not available'})
              # return HttpResponse(json_data, content_type='application/json', status=404)
              return self.render_to_http_response(json_data, status=404)
        else:
              json_data = self.serialize([emp,])      # SerialzeMixin Method
              # return HttpResponse(json_data, content_type='application/json', status=200)
              return self.render_to_http_response(json_data, status=200)

    def put(self, request,  id, *args, **kwargs):    #1st run these using testappm.py 
        emp = self.get_object_by_id(id)
        if emp is None:
              json_data = json.dumps({'msg':'No matched resource found so not possible to perform updation'})
              return self.render_to_http_response(json_data, status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
              json_data = json.dumps({'msg':'plz send valid json data only'})
              return self.render_to_http_response(json_data, status=400) 
        provided_data=json.loads(data)
        origianl_data = {
              'eno': emp.eno,
              'ename': emp.ename,
              'esal': emp.esal,
              'eaddr': emp.eaddr
        }
        origianl_data.update(provided_data)
        form = EmployeeForm(origianl_data, instance=emp)
        if form.is_valid():
              form.save(commit=True)
              json_data = json.dumps({'msg':'Resource updated successfully'})
              return self.render_to_http_response(json_data) 
        if form.errors:
              json_data = json.dumps(form.errors)
              return self.render_to_http_response(json_data, status=400)  
        

    def delete(self, request,  id, *args, **kwargs):    #1st run these using testappm.py 
        emp = self.get_object_by_id(id)
        if emp is None:
              json_data = json.dumps({'msg':'No matched resource found so not possible to perform deletion'})
              return self.render_to_http_response(json_data, status=404)
        status, deleted_item = emp.delete()
        if status == 1:
              json_data = json.dumps({'msg':'resource deleted successfully'})
              return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg':'unable to delete... plz try again'})
        return self.render_to_http_response(json_data)
"""
serialization -->
converting python dict object to json object
steps to do seriallization
1) python inbuilt module json
        json.dumps(data)

2) django serialize function
        for query set i.e. qs = Employee.objects.all()
        coverting list of employee objects into json there is an inbuilt module in "DJANGO" called as serializers
        there is serialize() method which query set into json data
        json_data = serializers.serialize('json', qs)..........from django.core.serializers import serialize

serialze used in above example for commented lines

3) by using rest_framework serializers
"""

# b) get all records

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(HttpResponseMixin, SerializeMixin, View):
        def get(self, request, *args, **kwargs):    #1st run these using testappm.py 
                qs = Employee.objects.all()          #employee Object data
                # json_data = serialize('json', qs)   # django serialize function
                json_data = self.serialize(qs)          # SerialzeMixin Method
                # return HttpResponse(json_data, content_type='application/json')
                return self.render_to_http_response(json_data, status=200)

        def post(self, request, *args, **kwargs):
                data = request.body
                valid_json = is_json(data)
                if not valid_json:
                      json_data = json.dumps({'msg':'plz send valid json data only'})
                      return self.render_to_http_response(json_data, status=400) 
                emp_data=json.loads(data)
                form = EmployeeForm(emp_data)
                if form.is_valid():
                      form.save(commit=True)
                      json_data = json.dumps({'msg':'Resource created successfully'})
                      return self.render_to_http_response(json_data) 
                if form.errors:
                      json_data = json.dumps(form.errors)
                      return self.render_to_http_response(json_data, status=400) 
"""
for post method it is neccessary to pass csrf token
in order to do post method without passing csrf sop there are three methods

1) method level --> (to disable csrf at method level)
                from django.views.decorators.csrf import csrf_exempt

                @csrf_exempt
                def my_view(request):
                        .....


2) class level --> (to disable at class level)
                from django.views.decorators.csrf import csrf_exempt
                from django.utils.decorators import method_decorator

                @method_decorator(csrf_exempt, name='dispatch')
                class EmlpoyeeListCBV(View):
                        ....
3) project level --> (to disable at project level)
                settings.py > middleware > comment csrf line
"""









"""
above two classes use twoendpoints in order to perform the crud operation but it is against standerd coding rules
we must only use only single endpoint in order to perform crud operation
"""
from django.views.generic import View
from testappm.models import Employee
from testappm.utils import is_json
from testappm.mixins import HttpResponseMixin, SerializeMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin, SerializeMixin, View):
        def get_object_by_id(self, id):
              try:
                    emp = Employee.objects.get(id=id)
              except Employee.DoesNotExist:
                    emp = None
              return emp
                    
        def get(self, request, *args, **kwargs):
              data = request.body
              valid_json = is_json(data)
              if not valid_json:
                    json_data = json.dumps({'msg':'plz send valid json data only'})
                    return self.render_to_http_response(json_data, status=400) 
              pdata = json.loads(data)
              id = pdata.get('id',None)
              if id is not None:
                    emp = self.get_object_by_id(id)
                    if emp is None:
                          json_data = json.dumps({'msg':'THe requested resource is not available with matched id'})
                          return self.render_to_http_response(json_data, status=404)
                    json_data = self.serialize([emp,])
                    return self.render_to_http_response(json_data, status=200)
              qs = Employee.objects.all()
              json_data = self.serialize(qs)          # SerialzeMixin Method
              return self.render_to_http_response(json_data, status=200)


        def post(self, request, *args, **kwargs):
              data = request.body
              valid_json = is_json(data)
              if not valid_json:
                    json_data = json.dumps({'msg':'plz send valid json data only'})
                    return self.render_to_http_response(json_data, status=400) 
              emp_data=json.loads(data)
              form = EmployeeForm(emp_data)
              if form.is_valid():
                    form.save(commit=True)
                    json_data = json.dumps({'msg':'Resource created successfully'})
                    return self.render_to_http_response(json_data) 
              if form.errors:
                    json_data = json.dumps(form.errors)
                    return self.render_to_http_response(json_data, status=400)
              

        def put(self, request, *args, **kwargs):
              data = request.body
              valid_json = is_json(data)
              if not valid_json:
                    json_data = json.dumps({'msg':'plz send valid json data only'})
                    return self.render_to_http_response(json_data, status=400) 
              pdata = json.loads(data)
              id = pdata.get('id',None)
              if id is None:
                    json_data = json.dumps({'msg':'provide id to perform updation'})
                    return self.render_to_http_response(json_data, status=400) 
              emp = self.get_object_by_id(id)
              if emp is None:
                    json_data = json.dumps({'msg':'No matched resource found so not possible to perform updation'})
                    return self.render_to_http_response(json_data, status=404) 
              provided_data=json.loads(data)
              origianl_data = {
              'eno': emp.eno,
              'ename': emp.ename,
              'esal': emp.esal,
              'eaddr': emp.eaddr
                 }
              origianl_data.update(provided_data)
              form = EmployeeForm(origianl_data, instance=emp)
              if form.is_valid():
                    form.save(commit=True)
                    json_data = json.dumps({'msg':'Resource updated successfully'})
                    return self.render_to_http_response(json_data) 
              if form.errors:
                    json_data = json.dumps(form.errors)
                    return self.render_to_http_response(json_data, status=400)  
                    
        def delete(self, request, *args, **kwargs):
              data = request.body
              valid_json = is_json(data)
              if not valid_json:
                    json_data = json.dumps({'msg':'plz send valid json data only'})
                    return self.render_to_http_response(json_data, status=400) 
              pdata = json.loads(data)
              id = pdata.get('id',None)
              if id is None:
                    json_data = json.dumps({'msg':'provide id to perform deletion'})
                    return self.render_to_http_response(json_data, status=400) 
              emp = self.get_object_by_id(id)
              if emp is None:
                    json_data = json.dumps({'msg':'No matched resource found so not possible to perform deletion'})
                    return self.render_to_http_response(json_data, status=404)
              status, deleted_item = emp.delete()
              if status == 1:
                    json_data = json.dumps({'msg':'resource deleted successfully'})
                    return self.render_to_http_response(json_data)
              json_data = json.dumps({'msg':'unable to delete... plz try again'})
              return self.render_to_http_response(json_data)
        


# go to 1_basic.txt Notes 
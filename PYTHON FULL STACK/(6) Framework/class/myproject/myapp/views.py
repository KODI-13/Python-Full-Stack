from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello welcome to my first project")

def homepage(request):
    return render(request, 'myapp/home.html')

def login(request):
    return render(request, 'myapp/login.html')

def staticpage(request):
    return render(request,'myapp/staticpractice.html')

def div(request):
    return render(request,'myapp/div.html')

def imvi(request):
    return render(request,'myapp/images&videos.html')

def zinza(request):
    data = {"name": "jay","age":21,"marks":79}
    context={
        "data":data
    }
    return render(request,'myapp/zinza.html',context)


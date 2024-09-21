from django.shortcuts import redirect, render
from student.models- import Student

# Create your views here.

def home(request):
    return render(request,'student/home.html')

def display(request):
    data=Student.objects.all()
    context={
        'data':data
    }
    return render(request,'student/display.html',context)

def registration(request):
    if request.method == 'POST':
        n=request.POST.get('name')
        c=request.POST.get('city')
        clg=request.POST.get('clg')
        d=request.POST.get('degree')
        y=request.POST.get('year')
        co=request.POST.get('course')
        data = Student(name=n,city=c,college=clg,degree=d,year=y,course=co)
        data.save()
    return render(request,'student/registration.html')

def update(request,id):
    data=Student.objects.get(id=id)
    context={
        'data':data
    }
    if request.method == 'POST':
        n=request.POST.get('name')
        c=request.POST.get('city')
        clg=request.POST.get('clg')
        d=request.POST.get('degree')
        y=request.POST.get('year')
        co=request.POST.get('course')
        data.name = n
        data.city = c
        data.college = clg
        data.degree = d
        data.year = y
        data.course = co
        data.save()
    return render(request,'student/update.html',context)

def delete(request,id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('/display/')

def about(request):
    return render(request,'student/about.html')
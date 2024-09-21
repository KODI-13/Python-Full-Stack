from django.http import HttpResponse
from django.shortcuts import redirect, render

from hotel.models import Customer

# Create your views here.

King_room = 10
queen_room = 10
suit_room = 10
single_room = 10
double_room = 10
triple_room = 10

def home(request,id):
    if request.method == 'POST':
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.get(id=id)

                context = {
                    'data':data,
                }
                return redirect('/booking/',context)
    return render(request,'hotel/home.html')

def gallery(request):
    return render(request,'hotel/gallery.html')

def about(request):
    return render(request,'hotel/about.html')

def contact(request):
    return render(request,'hotel/contact.html')

def booking(request,id):
    data=Customer.objects.get(id=id)
    context={
        'data':data
    }
    return render(request,'hotel/booking.html',context)



def king(request):
    if request.method == 'POST':
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                context = {
                    'data':data,
                }
                return render(request,'hotel/booking.html',context)
    return render(request,'hotel/king.html')

def queen(request):
    if request.method == 'POST':
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                context = {
                    'data':data,
                }
                return render(request,'hotel/booking.html',context)
    return render(request,'hotel/queen.html')

def suit(request):
    if request.method == 'POST':
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                context = {
                    'data':data,
                }
                return render(request,'hotel/booking.html',context)
    return render(request,'hotel/suit.html')

def single(request):
    if request.method == 'POST':
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                context = {
                    'data':data,
                }
                return render(request,'hotel/booking.html',context)
    return render(request,'hotel/single.html')

def double(request):
    if request.method == 'POST':
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                context = {
                    'data':data,
                }
                return render(request,'hotel/booking.html',context)
    return render(request,'hotel/double.html')

def triple(request):
    if request.method == 'POST':
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                context = {
                    'data':data,
                }
                return render(request,'hotel/booking.html',context)
    return render(request,'hotel/triple.html')
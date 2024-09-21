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

def home(request):
    return render(request,'hotel/home.html')

def gallery(request):
    return render(request,'hotel/gallery.html')

def about(request):
    return render(request,'hotel/about.html')

def contact(request):
    return render(request,'hotel/contact.html')

def booking(request):
    if request.method == 'POST':

        if 'button1' in request.POST:
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                saved_id = data.id
                data = Customer.objects.all()

                button_clicked1 = 'button1'
                context = {
                    'data':data,
                    'button_clicked1' : button_clicked1,
                    'saved_id' : saved_id
                }
                return render(request,'hotel/booking.html',context)
        
        elif 'button2' in request.POST:
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                button_clicked1 = 'button2'
                context = {
                    'data':data,
                    'button_clicked1' : button_clicked1
                }
                return render(request,'hotel/booking.html',context)
        
        elif 'button3' in request.POST:
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                button_clicked1 = 'button3'
                context = {
                    'data':data,
                    'button_clicked1' : button_clicked1
                }
                return render(request,'hotel/booking.html',context)
        
        elif 'button4' in request.POST:
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                button_clicked1 = 'button4'
                context = {
                    'data':data,
                    'button_clicked1' : button_clicked1
                }
                return render(request,'hotel/booking.html',context)
        
        elif 'button5' in request.POST:
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                button_clicked1 = 'button5'
                context = {
                    'data':data,
                    'button_clicked1' : button_clicked1
                }
                return render(request,'hotel/booking.html',context)
        
        elif 'button6' in request.POST:
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                button_clicked1 = 'button6'
                context = {
                    'data':data,
                    'button_clicked1' : button_clicked1
                }
                return render(request,'hotel/booking.html',context)
        
        else:
                cid = request.POST.get('CheckInDate')
                cod = request.POST.get('CheckOutDate')
                cc = request.POST.get('ChildCount')
                ac = request.POST.get('AdultCount')
                data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
                data.save()
                data = Customer.objects.all()
                button_clicked1 = 'button7'
                context = {
                    'data':data,
                    'button_clicked1' : button_clicked1
                }
                return render(request,'hotel/booking.html',context)
    return render(request,'hotel/booking.html')



def king(request):
    return render(request,'hotel/king.html')

def queen(request):
    return render(request,'hotel/queen.html')

def suit(request):
    return render(request,'hotel/suit.html')

def single(request):
    return render(request,'hotel/single.html')

def double(request):
    return render(request,'hotel/double.html')

def triple(request):
    # if request.method == 'POST':
    #     cid = request.POST.get('CheckInDate')
    #     cod = request.POST.get('CheckOutDate')
    #     cc = request.POST.get('ChildCount')
    #     ac = request.POST.get('AdultCount')
    #     data = Customer(Check_In_Date=cid, Check_Out_Date=cod, Child_Count=cc, Adult_Count=ac)
    #     data.save()
    #     return redirect('/booking/')
    return render(request,'hotel/triple.html')
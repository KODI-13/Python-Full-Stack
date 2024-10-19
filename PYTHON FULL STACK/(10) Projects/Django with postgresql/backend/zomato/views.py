from django.shortcuts import render
from zomato.models import OrderItem


# Create your views here.
def show_details(request):
    queryset = OrderItem.objects.all()
    context = {
        'data':queryset
    }
    return render(request, 'zomato/home.html', context)


from django.shortcuts import render
import requests

# Create your views here.
def get_geographic_info(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR', "") or request.META.get('REMOTE_ADDR')
    url = 'http://api.ipstack.com/172.69.223.142?access_key=5166deec030c6a22421bee4e2da1ee33'
    # url = 'http://api.ipstack.com/'+str(ip)+'?access_key=5166deec030c6a22421bee4e2da1ee33'
    response = requests.get(url)
    data = response.json()
    return render(request,'testapps/info.html', data)


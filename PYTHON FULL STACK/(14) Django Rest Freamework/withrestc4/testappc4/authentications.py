from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CutomAuthenticatation(BaseAuthentication):          # it is neccessary to be child class of BaseAuthenticatation
    def authenticate(self, request):             # we have to override authenticate method
        username = request.GET.get('username')
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)  # this lines means in User table is there any reord with username as provided username i.e.(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('Your credentials are invalid , plz provide valid credentials to access endpoints')
        return (user, None)
    

class CutomAuthenticatation2(BaseAuthentication):          # it is neccessary to be child class of BaseAuthenticatation
    def authenticate(self, request):             # we have to override authenticate method
        username = request.GET.get('username')
        key=request.GET.get('key')
        if username is None or key is None:
            return None
        c1 = len(key) == 7
        c2 = key[0] == username[-1].lower()
        c3 = key[2] == 'Z'
        c4 = key[4] == username[0]
        try:
            user = User.objects.get(username=username)  # this lines means in User table is there any reord with username as provided username i.e.(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('Your provided username is invalid , plz provide valid username')
        if c1 and c2 and c3 and c4:
            return (user , None)
        raise AuthenticationFailed('Your provided is invalid , plz provide valid key to access endpoints')
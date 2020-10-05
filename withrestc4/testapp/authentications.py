from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
class CustomAuthentication(BaseAuthentication):
        def authenticate(self,request):
            username = request.GET.get('username')
            print(username)
            if username is None:
                return
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise AuthenticationFailed('Your credintials invalid..  please provide valid ones to access point...')
            return (user,None)

class CustomAuthentication2(BaseAuthentication):
    def authenticate(self,request):
        username = request.GET.get('username')
        key = request.GET.get('key')
        if username is None or key is None:
            return None
        c1 = len(key) == 7 # i7ZXH98
        c2 = key[0] == username[-1].lower() # i
        c3 = key[2] == "Z" # Z
        c4 = key[4] == username[0] # H
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('Provided username not exists ')

        if c1 and c2 and c3 and c4:
            return (user,None)
        raise  AuthenticationFailed('Your credintials invalid..  please provide valid ones to access point...')

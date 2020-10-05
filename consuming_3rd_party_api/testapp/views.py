from django.shortcuts import render
import requests
# Create your views here.

'''
https://ipstack.com/quickstart
IPSTACK API details
api-key:  88398224465e431ba9edeea1067d0a51
http://api.ipstack.com/157.48.206.14?access_key=88398224465e431ba9edeea1067d0a51&format=1
'''
def get_geographi_info(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    url = "http://api.ipstack.com/157.48.206.14?access_key=88398224465e431ba9edeea1067d0a51"
    # url = 'http://api.ipstack.com/ '+str(ip)+'?access_key=88398224465e431ba9edeea1067d0a51'
    response = requests.get(url)
    data = response.json()
    return render(request,'testapp/info.html',data)



# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

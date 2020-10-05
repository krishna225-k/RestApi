
import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

# def get_resource(id=None):
#     data = {}
#     if id is not None:
#         data = {
#         'id': id
#         }
#
#     resp = requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     # print(resp.text)
#     print(resp.status_code)
#     print(resp.json())
# get_resource(4)
# get_resource()
# # get_resource(10)

def create_resource():
    new_emp = {
    'eno':19,
    'ename':'Modhin',
    'esal':7000,
    'eaddr':'delhi'
    }
    # resp = requests.post(BASE_URL+ENDPOINT,data=new_data)
    resp = requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp)) # valid formate
    print(resp.status_code)
    print(resp.json())
create_resource()

# import requests
# import json
# BASE_URL = 'http://127.0.0.1:8000/'
# # ENDPOINT = 'formvalidation/'
# ENDPOINT = 'api/'
# def update_resource(id):
#     new_data = {
#     'id':id, # all fields need to pass, if you no pass the all fields then , put method serializer objects shoud be partial=True
#     'eno':720,
#     'ename':'Ramana',
#     'esal':2500,
#     }
#     # resp = requests.post(BASE_URL+ENDPOINT,data=new_data)
#     resp = requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data)) # valid formate
#     # print(resp.status_code)
#     print(resp.json())
# update_resource(3)
# update_resource(80)

#  multiple level validations
# def update_resource(id):
#     new_data = {
#     'id':id, # all fields need to pass, if you no pass the all fields then , put method serializer objects shoud be partial=True
#     'eno':777,
#     'ename':'Varun',
#     'esal':2500,
#     }
#     # resp = requests.post(BASE_URL+ENDPOINT,data=new_data)
#     resp = requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data)) # valid formate
#     # print(resp.status_code)
#     print(resp.json())
# update_resource(3)

# def update_resource(id):
#     new_data = {
#     'id':id, # all fields need to pass, if you no pass the all fields then , put method serializer objects shoud be partial=True
#     'eno':777,
#     'ename':'Varun', # both ename and esal both field was validatation happend
#     'esal':50001,
#     }
#     # resp = requests.post(BASE_URL+ENDPOINT,data=new_data)
#     resp = requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data)) # valid formate
#     # print(resp.status_code)
#     print(resp.json())
# update_resource(3)


# def update_resource(id):
#     new_data = {
#     'id':id, # all fields need to pass, if you no pass the all fields then , put method serializer objects shoud be partial=True
#     'eno':777,
#     'ename':'Ramana' ,            # both ename and esal both field was validatation happend
#     'esal':5001, # varifing the validation by using with validater with priority
#     }
#     # resp = requests.post(BASE_URL+ENDPOINT,data=new_data)
#     resp = requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data)) # valid formate
#     # print(resp.status_code)
#     print(resp.json())
# update_resource(3)



# def delete_resource(id):
#     data = {
#     'id':id
#     }
#     resp = requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data)) # valid formate
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(5)

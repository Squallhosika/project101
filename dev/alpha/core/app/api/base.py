# from external.userApp import call_function
import requests
API_BASE_URL = 'http://127.0.0.1:8000/'
API_CLIENT_URL = 'http://127.0.0.1:8000/'
API_USER_URL = 'http://127.0.0.1:8002/'
API_ORDER_URL = 'http://127.0.0.1:8003/'

def call_function(method_name, service_name, function_name, params=None):
    url = get_url(service_name, function_name)

    if method_name == 'GET':        req = requests.get(url, data=params)
    elif method_name == 'POST':     req = requests.post(url, data=params)
    elif method_name == 'PUT':      req = requests.put(url, data=params)
    elif method_name == 'DELETE':   req = requests.delete(url, data=params)

    return req

def get_url(service_name, function_name):
    if service_name == 'client':    url = API_CLIENT_URL
    elif service_name == 'user':    url = API_USER_URL
    elif service_name == 'order':   url = API_ORDER_URL

    return url + service_name + '/' + function_name + '/'

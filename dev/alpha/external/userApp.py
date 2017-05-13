import requests
API_BASE_URL = 'http://127.0.0.1:8000/'
API_CLIENT_URL = 'http://127.0.0.1:8000/'
API_USER_URL = 'http://127.0.0.1:8000/'

def get(name, **kwargs):

    if name == 'items':     req = requests.get(API_BASE_URL + 'items/' + str(kwargs.get('id','')))
    if name == 'menus':     req = requests.get(API_BASE_URL + 'menus/' + str(kwargs.get('id','')))
    if name == 'clients':   req = requests.get(API_BASE_URL + 'clients/' + str(kwargs.get('id','')))

    return req

def getJSON(object, **kwargs):

    if object == 'items':     req = requests.get(API_BASE_URL + 'items/' + str(kwargs.get('id','')))
    if object == 'menus':     req = requests.get(API_BASE_URL + 'menus/' + str(kwargs.get('id','')))
    if object == 'clients':   req = requests.get(API_BASE_URL + 'clients/' + str(kwargs.get('id','')))

    return req.json()

def create(object, **kwargs):
    json = '{"name": "' + str(kwargs.get('name','')) + '"}'
    data = {'name': str(kwargs.get('name',''))}
    req = requests.post(API_BASE_URL + 'items/',data=data)

    if object == 'items':     req = requests.get(API_BASE_URL + 'items/' + str(kwargs.get('id','')))



def call_function(method_name, service_name, function_name, params=None):
    url = get_url(service_name, function_name)

    if method_name == 'GET':        req = requests.get(url, params=params)
    elif method_name == 'POST':     req = requests.post(url, data=params)

    return req.json()

def get_url(service_name, function_name):
    if service_name == 'client':    url = API_CLIENT_URL
    elif service_name == 'user':    url = API_USER_URL

    return url + service_name + '/' + function_name + '/'




if __name__ == '__main__':

    service_name = 'client'
    function_name = 'items'
    req0_json = call_function('GET', service_name, function_name)
    print(req0_json)

    params = {'name': 'item4'}
    req1_json = call_function('POST', service_name, function_name, params)
    req2_json = call_function('GET', service_name, function_name)
    print(req2_json)

    # req1 = get('items', id=1)
    # req1_json = getJSON('items')
    # print(req1_json)
    #
    # create('items', name='item3')
    # req2_json = getJSON('items')
    # print(req2_json)
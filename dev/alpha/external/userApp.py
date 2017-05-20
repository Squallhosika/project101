import requests
API_BASE_URL = 'http://127.0.0.1:8000/'
API_CLIENT_URL = 'http://127.0.0.1:8001/'
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






if __name__ == '__main__':

    service_name = 'client'
    function_name = 'removemenuclient'
    # params = {'item_id': 9, 'menu_id': 1, 'price': 1}
    # params = {'id': 2, 'name': 'menu2'}
    # params = {'menu_id': 2}
    params = {'id': 3}

    # req0 = call_function('GET', service_name, function_name, params)
    # req0 = call_function('POST', service_name, function_name, params)
    # req0 = call_function('PUT', service_name, function_name, params)
    req0 = call_function('DELETE', service_name, function_name, params)
    print(req0.status_code)
    # print(req0.json())

    # req1 = call_function('GET', service_name, 'clients')
    # print(req1.json())

    # params = {'name': 'item4'}
    # req1 = call_function('POST', service_name, function_name, params)

    # params = {'id': '5'}
    # req1 = call_function('DELETE', service_name, function_name, params)
    # req2 = call_function('GET', service_name, function_name)
    # print(req1.status_code)
    # print(req2.json())

    # req1 = get('items', id=1)
    # req1_json = getJSON('items')
    # print(req1_json)
    #
    # create('items', name='item3')
    # req2_json = getJSON('items')
    # print(req2_json)
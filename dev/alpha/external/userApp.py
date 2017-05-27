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


def client_around():
    service_name = 'client'
    function_name = 'clientaround'

    req0 = call_function('GET', service_name, function_name)
    return req0.json()

def get_menu(client_id):
    service_name = 'client'

    function_name = 'getmenu'
    params = {'client_id': client_id}

    req0 = call_function('GET', service_name, function_name, params)
    # c=req0.json()
    menu_id = req0.json()[0]['menu_id']

    function_name = 'getitems'
    params = {'menu_id': menu_id}

    req1 = call_function('GET', service_name, function_name, params)
    # c = req1.json()
    return req1.json()



def create_order(items):
    service_name = 'order'

    function_name = 'createorder'
    client_id = items[0]['client_id']
    params = {'user_id': 1, 'client_id': client_id}

    req0 = call_function('POST', service_name, function_name, params)
    order_id = req0.json()[0]['id']

    for item in items:
        item_id = item['item_id']
        price = item['price']
        qty = item['qty']

        function_name = 'orderadditem'
        params = {'item_id': 1, 'order_id': order_id, 'price': price, 'quantity': qty}

        req1 = call_function('POST', service_name, function_name, params)
        # call_function('POST', 'order', 'orderadditem', {'item_id': 1, 'order_id': order_id, 'price': 2.5, 'quantity': 4})

    function_name = 'placeorder'
    params = {'order_id': order_id}

    req2 = call_function('POST', service_name, function_name, params)
    return req2.json()



# if __name__ == '__main__':
#
#     service_name = 'client'
#     function_name = 'removemenuclient'
#     # params = {'item_id': 9, 'menu_id': 1, 'price': 1}
#     # params = {'id': 2, 'name': 'menu2'}
#     # params = {'menu_id': 2}
#     params = {'id': 3}
#
#     # req0 = call_function('GET', service_name, function_name, params)
#     # req0 = call_function('POST', service_name, function_name, params)
#     # req0 = call_function('PUT', service_name, function_name, params)
#     req0 = call_function('DELETE', service_name, function_name, params)
#     print(req0.status_code)
#     # print(req0.json())
#
#     # req1 = call_function('GET', service_name, 'clients')
#     # print(req1.json())
#
#     # params = {'name': 'item4'}
#     # req1 = call_function('POST', service_name, function_name, params)
#
#     # params = {'id': '5'}
#     # req1 = call_function('DELETE', service_name, function_name, params)
#     # req2 = call_function('GET', service_name, function_name)
#     # print(req1.status_code)
#     # print(req2.json())
#
#     # req1 = get('items', id=1)
#     # req1_json = getJSON('items')
#     # print(req1_json)
#     #
#     # create('items', name='item3')
#     # req2_json = getJSON('items')
#     # print(req2_json)
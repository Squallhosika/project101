import json

from core.app.api.base import call_function

class UserApp():
    def __init__(self, user_id):
        self.user_id = user_id
        # self.location = 1

    def client_around(self):
        service_name = 'client'
        function_name = 'clientaround'

        req0 = call_function('GET', service_name, function_name)
        return req0.json()

    def client_pending_orders(self):
        service_name = 'order'
        function_name = 'orders'

        req0 = call_function('GET', service_name, function_name)
        return req0.json()

    def get_menu(self,client_id):
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

    def create_order(self, items):
        service_name = 'order'

        function_name = 'createorder'
        client_id = items[0]['client_id']
        params = {'user_id': 1, 'client_id': client_id}

        req0 = call_function('POST', service_name, function_name, params)
        dsds = req0.text
        de=json.loads(dsds)
        order_id = de['id']
        # order_id = c['id']

        ct=0
        for item in items:
            item_id = item['item_id']
            price = item['price']
            qty = item['qty']

            if int(qty) > 0:
                function_name = 'orderadditem'
                params = {'item_id': item_id, 'order_id': order_id, 'price': price, 'quantity': qty}

                req1 = call_function('POST', service_name, function_name, params)
                ct=ct+1
            # call_function('POST', 'order', 'orderadditem', {'item_id': 1, 'order_id': order_id, 'price': 2.5, 'quantity': 4})

        function_name = 'placeorder'
        params = {'order_id': order_id}

        if ct > 0:
            req2 = call_function('POST', service_name, function_name, params)
            return req2.json()


#
# def client_around():
#     service_name = 'client'
#     function_name = 'clientaround'
#
#     req0 = call_function('GET', service_name, function_name)
#     return req0.json()
#
# def client_pending_orders():
#     service_name = 'order'
#     function_name = 'orders'
#
#     req0 = call_function('GET', service_name, function_name)
#     return req0.json()
#
# def get_menu(client_id):
#     service_name = 'client'
#
#     function_name = 'getmenu'
#     params = {'client_id': client_id}
#
#     req0 = call_function('GET', service_name, function_name, params)
#     # c=req0.json()
#     menu_id = req0.json()[0]['menu_id']
#
#     function_name = 'getitems'
#     params = {'menu_id': menu_id}
#
#     req1 = call_function('GET', service_name, function_name, params)
#     # c = req1.json()
#     return req1.json()
#
#
#
# def create_order(items):
#     service_name = 'order'
#
#     function_name = 'createorder'
#     client_id = items[0]['client_id']
#     params = {'user_id': 1, 'client_id': client_id}
#
#     req0 = call_function('POST', service_name, function_name, params)
#     dsds = req0.text
#     de=json.loads(dsds)
#     order_id = de['id']
#     # order_id = c['id']
#
#     ct=0
#     for item in items:
#         item_id = item['item_id']
#         price = item['price']
#         qty = item['qty']
#
#         if int(qty) > 0:
#             function_name = 'orderadditem'
#             params = {'item_id': item_id, 'order_id': order_id, 'price': price, 'quantity': qty}
#
#             req1 = call_function('POST', service_name, function_name, params)
#             ct=ct+1
#         # call_function('POST', 'order', 'orderadditem', {'item_id': 1, 'order_id': order_id, 'price': 2.5, 'quantity': 4})
#
#     function_name = 'placeorder'
#     params = {'order_id': order_id}
#
#     if ct > 0:
#         req2 = call_function('POST', service_name, function_name, params)
#         return order_id #req2.json()
#
#
#
# # if __name__ == '__main__':
# #
# #     service_name = 'client'
# #     function_name = 'removemenuclient'
# #     # params = {'item_id': 9, 'menu_id': 1, 'price': 1}
# #     # params = {'id': 2, 'name': 'menu2'}
# #     # params = {'menu_id': 2}
# #     params = {'id': 3}
# #
# #     # req0 = call_function('GET', service_name, function_name, params)
# #     # req0 = call_function('POST', service_name, function_name, params)
# #     # req0 = call_function('PUT', service_name, function_name, params)
# #     req0 = call_function('DELETE', service_name, function_name, params)
# #     print(req0.status_code)
# #     # print(req0.json())
# #
# #     # req1 = call_function('GET', service_name, 'clients')
# #     # print(req1.json())
# #
# #     # params = {'name': 'item4'}
# #     # req1 = call_function('POST', service_name, function_name, params)
# #
# #     # params = {'id': '5'}
# #     # req1 = call_function('DELETE', service_name, function_name, params)
# #     # req2 = call_function('GET', service_name, function_name)
# #     # print(req1.status_code)
# #     # print(req2.json())
# #
# #     # req1 = get('items', id=1)
# #     # req1_json = getJSON('items')
# #     # print(req1_json)
# #     #
# #     # create('items', name='item3')
# #     # req2_json = getJSON('items')
# #     # print(req2_json)
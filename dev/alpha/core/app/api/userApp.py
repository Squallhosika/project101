import json

from core.app.api.base import call_function

class UserApp():
    def __init__(self, user_id, latitude=-0.075835, longitude=51.521456, radius=0.5):
        self.user_id = user_id
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.radius = radius

        # self.location = 1

    # def client_around(self):
    #     service_name = 'client'
    #     function_name = 'clientaround'
    #
    #     req0 = call_function('GET', service_name, function_name)
    #     return req0.json()

    def client_around(self):
        service_name = 'geo'
        function_name = 'clientsaround'

        params = {'latitude': self.latitude, 'longitude': self.longitude, 'radius': self.radius}
        # print(params)

        req0 = call_function('GET', service_name, function_name, params)
        return req0.json()
        # return req0.json()

    def client_pending_orders(self):
        service_name = 'order'
        function_name = 'orders'

        req0 = call_function('GET', service_name, function_name)
        return req0.json()

    def user_created_orders(self):
        pass

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
        # client_id = items[0]['client_id']
        item1 = items[next(iter(items))]
        client_id = item1['client_id']
        menu_id = item1['menu_id']
        shift_id = item1['shift_id']
        params = {'user_id': 1, 'client_id': client_id, 'shift_id': shift_id, 'menu_id': menu_id}

        req0 = call_function('POST', service_name, function_name, params)
        dsds = req0.text
        de = json.loads(dsds)
        order_id = de['id']

        # Actualy this is done in the service order
        # params_queue = {'master_id': shift_id, 'type': 'pending', 'id': order_id, 'time': 2.5, 'rating': 2.5}
        # req_queue = call_function('POST', 'dqueue', 'createnode', )

        # order_id = c['id']

        ct=0
        for item_id, item in items.items():
            # item_id = item['item_id']
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
            #TODO
            pass
            # req2 = call_function('POST', service_name, function_name, params)
            # return req2.json()

    def get_active_shift_id(self, client_id):
        service_name = 'client'
        function_name = 'shiftbyclientstatus'

        params = {'client_id': client_id, 'status': 'active'}

        items = call_function('GET', service_name, function_name, params)
        res = items.json()
        if len(res) != 1:
            raise Exception('For now client should have only 1 active shift.'
                            + 'This is not the case for the clientID', client_id)
        return res[0]['id']

    #GET USERS
    def get_all_users(self):
        service_name = 'client'
        function_name = 'users'
        users = []
        users.append({'id':1})
        users.append({'id':2})
        users.append({'id':3})

        return users
        # clients = call_function('GET', service_name, function_name)
        # return clients.json()


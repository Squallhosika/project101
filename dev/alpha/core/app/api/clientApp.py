from core.app.api.base import call_function

class ClientApp():

    def __init__(self, client_id) : #, shift_id):
        self.client_id = client_id


    #GET ORDERS
    def get_pending_orders(self):
        return self.get_orders_by_status('created')

    def get_validated_orders(self):
        return self.get_orders_by_status('validated')


    def get_orders_by_status(self, status):
        service_name = 'order'
        function_name = 'orderbyclientstatus'
        params = {'client_id': self.client_id, 'status': status}

        orders = call_function('GET', service_name, function_name, params)
        return orders.json()


    #UPDATE ORDERS STATUS
    def validate_orders(self, order_ids):
        orders = {}
        for order_id in order_ids:
            orders[order_id] = self.update_order_status(order_id, 'validated')

        return orders


    def update_order_status(self, order_id, status):
        service_name = 'order'
        function_name = 'ordervalidate'

        params = {'id': order_id, 'status': status}
        order = call_function('PUT', service_name, function_name, params)

        return order.json()


    #GET CLIENTS
    def get_all_clients(self):
        service_name = 'client'
        function_name = 'clients'

        clients = call_function('GET', service_name, function_name)
        return clients.json()


class Jo():

    def get_pending_orders(self):

        orders = self.get_orders_by_status('created')

        self.pending_orders = []
        for order in orders.json():
            order_id = order['id']
            self.pending_orders.append(order_id)

        return self.pending_orders

    def get_validated_orders(self):

        orders = self.get_orders_by_status('validated')

        self.validated_orders = []
        for order in orders.json():
            order_id = order['id']
            self.validated_orders.append(order_id)

        return self.validated_orders


    def update_pending_order(self):
        req_new_orders = call_function('GET', 'order', 'neworders', {'client_id': self.client_id})
        self.pending_order = req_new_orders.json()

    def next_pending_order(self):
        return min(self.pending_order, lambda po: po['rank'])

    def validate_next_pending_order(self):
        order = self.next_pending_order()
        call_function('PUT', 'order', 'orderacceptedbyclient', {'order_id': order['order_id']})

    def reject_next_pending_order(self):
        order = self.next_pending_order()
        call_function('PUT', 'order', 'orderrejectedbyclient', {'order_id': order['order_id']})

    def update_beingserve_order(self):
        req_new_orders = call_function('GET', 'order', 'beingserveorder', {'client_id': self.client_id})
        self.beingserve_order = req_new_orders.json()

    def complete_order(self, order_id):
        call_function('PUT', 'order', 'order_completed', {'order_id': order_id})
        self.beingserve_order = filter(lambda x: x['order_id'] == order_id, self.beingserve_order)

    def complete_order_by_employee_id(self, employee_id):
        order_id = filter(lambda x: x['employee_id'] == employee_id, self.beingserve_order)[0]['order_id']
        self.complete_order(order_id)

    def attribute_next_order(self, employee_id):
        order = call_function('GET', 'order', 'nexttoserve', {'client_id': self.client_id, 'employee_id': employee_id})
        self.beingserve_order.append(order.json())
        return order

    def update_inqueue_order(self):
        req_inqueue_orders = call_function('GET', 'order', 'inqueueorder', {'client_id': self.client_id})
        self.inqueue_order = req_inqueue_orders.json()

    def add_employee_to_shift(self, employee_id):
        call_function('POST', 'client', 'addemployeetoshift',
                      {"employee_id": employee_id,  "shift_id": self.shift_id, "status": ""})
        self.active_employees.append(employee_id)

    def remove_employee_from_shift(self, employee_id):
        call_function('DELETE', 'client', 'removeemployeefromshift', {'employee_id': employee_id})
        self.active_employees.remove(employee_id)

    def update_active_employees(self):
        employees = call_function('GET', 'client', 'getemployeesfromshift', {'shift_id': self.shift_id})
        self.active_employees = [employee['id'] for employee in employees]



if __name__ == "__main__":
    clientAPP = ClientApp(1)
    clientAPP.validate_orders([1])
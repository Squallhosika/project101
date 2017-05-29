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


class ClientApp:

    def __init__(self, client_id):
        self.client_id = client_id
        # TODO implement a logic for the shift
        self.shift_id = client_id
        self.pending_order = []
        self.beingserve_order = []
        self.inqueue_order = []
        self.active_employees = []
        self.update_pending_order()
        self.update_beingserve_order()
        self.update_inqueue_order()
        # self.update_active_employees()

    @staticmethod
    def orders_to_ids(key, orders):
        return [order[key] for order in orders]

    def pending_order_ids(self):
        return self.orders_to_ids('order_id', self.pending_order)

    def beingserve_order_ids(self):
        return self.orders_to_ids('order_id', self.beingserve_order)

    def inqueue_order_ids(self):
        return self.orders_to_ids('order_id', self.inqueue_order)

    def update_pending_order(self):
        req_new_orders = call_function('GET', 'order', 'neworders', {'client_id': self.client_id})
        self.pending_order = req_new_orders.json()

    def next_pending_order(self):
        return min(self.pending_order, key=lambda po: po.get('rank'))

    def validate_next_pending_order(self):
        order = self.next_pending_order()
        call_function('PUT', 'order', 'orderacceptedbyclient', {'order_id': order['order_id']})
        self.update_pending_order()

    def reject_next_pending_order(self):
        order = self.next_pending_order()
        call_function('PUT', 'order', 'orderrejectedbyclient', {'order_id': order['order_id']})
        self.update_pending_order()

    def update_beingserve_order(self):
        req_new_orders = call_function('GET', 'order', 'beingserveorders', {'client_id': self.client_id})
        self.beingserve_order = req_new_orders.json()

    def complete_order(self, order_id):
        call_function('PUT', 'order', 'ordercompleted', {'order_id': order_id})
        list_completed = list(filter(lambda x: x['order_id'] == order_id, self.beingserve_order))
        self.beingserve_order.remove(list_completed[0])

    def complete_order_by_employee_id(self, employee_id):
        list_order = list(filter(lambda x: x['employee_id'] == employee_id, self.beingserve_order))
        order_id = list_order[0]['order_id']
        self.complete_order(order_id)

    def attribute_next_order(self, employee_id):
        order = call_function('PUT', 'order', 'nexttoserve', {'client_id': self.client_id, 'employee_id': employee_id})
        self.beingserve_order.append(order.json())
        self.update_inqueue_order()
        return order

    def update_inqueue_order(self):
        req_inqueue_orders = call_function('GET', 'order', 'inqueueorders', {'client_id': self.client_id})
        self.inqueue_order = req_inqueue_orders.json()

    def add_employee_to_shift(self, employee_id):
        call_function('POST', 'client', 'addemployeetoshift',
                      {"employee_id": employee_id, "shift_id": self.shift_id, "status": ""})
        self.active_employees.append(employee_id)

    def remove_employee_from_shift(self, employee_id):
        call_function('DELETE', 'client', 'removeemployeefromshift',
                      {"shift_id": self.shift_id, 'employee_id': employee_id})
        self.active_employees.remove(employee_id)

    def update_active_employees(self):
        employees = call_function('GET', 'client', 'getemployeesfromshift', {'shift_id': self.shift_id})
        self.active_employees = [employee['id'] for employee in employees.json()]
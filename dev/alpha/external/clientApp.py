from external.userApp import call_function

class ClientApp():

    def __init__(self, client_id, shift_id):
        self.client_id = client_id
        self.shift_id = shift_id
        self.pending_order = None
        self.beingserve_order = None
        self.inqueue_order = None
        self.active_employees = []
        self.update_pending_order()
        # self.update_beingserve_order()
        # self.update_inqueue_order()
        # self.update_active_employees()

    def update_pending_order(self):
        req_new_orders = call_function('GET', 'order', 'neworders', {'client_id': self.client_id})
        self.pending_order = req_new_orders.json()

    def next_pending_order(self):
        return min(self.pending_order, key=lambda po: po.get('rank'))

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
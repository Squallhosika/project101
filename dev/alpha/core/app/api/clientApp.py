from core.app.api.base import call_function

class ClientApp():

    def __init__(self, client_id):
        self.client_id = client_id
        self.shift_id = None
        self.menu_id = None
        self.init_shift()


    #GET ORDERS
    def get_pending_orders(self):
        return self.get_orders_by_status('created')

    def get_validated_orders(self):
        return self.get_orders_by_status('validated')

    def get_pickup_orders(self):
        return self.get_orders_by_status('pickup')

    def get_orders_by_status(self, status):
        service_name = 'order'
        function_name = 'orderbyclientstatus'
        params = {'client_id': self.client_id, 'status': status}

        orders = call_function('GET', service_name, function_name, params)
        return orders.json()

    #GET EMPLOYEES
    def get_available_employees(self):
        return self.get_employees_by_status('available')

    def get_employees_by_status(self, status):
        service_name = 'client'
        function_name = 'employeebyclientstatus'
        params = {'client_id': self.client_id, 'status': status}
        # params = {'client_id': self.client_id}

        employees = call_function('GET', service_name, function_name, params)
        return employees.json()

    def get_employees_in_shift(self):
        employees = call_function('GET', 'client', 'getemployeesfromshift', {'shift_id': self.shift_id})
        return employees.json()

    #GET SHIFTS
    def get_all_shifts(self):
        return self.get_shifts_by_status('all')

    def get_active_shifts(self):
        return self.get_shifts_by_status('active')

    def get_inactive_shifts(self):
        return self.get_shifts_by_status('inactive')

    def get_shifts_by_status(self, status):
        service_name = 'client'
        function_name = 'shiftbyclientstatus'
        params = {'client_id': self.client_id, 'status': status}
        # params = {'client_id': self.client_id}

        shifts = call_function('GET', service_name, function_name, params)
        return shifts.json()


    #UPDATE ORDERS STATUS
    def validate_orders(self, order_ids):
        orders = {}
        for order_id in order_ids:
            orders[order_id] = self.update_order_status(order_id, 'validated')

        return orders

    def reject_orders(self, order_ids):
        orders = {}
        for order_id in order_ids:
            orders[order_id] = self.update_order_status(order_id, 'rejected')

        return orders

    def pickup_orders(self, order_ids):
        orders = {}
        for order_id in order_ids:
            orders[order_id] = self.update_order_status(order_id, 'pickup')

        return orders

    def update_order_status(self, order_id, status):
        service_name = 'order'

        if status == 'validated':
            function_name = 'ordervalidate'
        elif status == 'pickup':
            function_name = 'orderpickup'

        params = {'id': order_id, 'status': status}
        order = call_function('PUT', service_name, function_name, params)

        return order.json()


    #UPDATE SHIFTS STATUS
    def init_shift(self):
        active_shifts = self.get_active_shifts()
        if len(active_shifts) > 0:
            self.shift_id = active_shifts[0]['id']
            return
        shifts = self.get_all_shifts()
        self.activate_shift(shifts[0]['id'])


    def activate_shift(self, shift_id):
        if self.shift_id:
            self.update_shift_status(self.shift_id, 'inactive')

        self.update_shift_status(shift_id, 'active')
        self.shift_id = shift_id

    def activate_shifts(self, shift_ids):
        shifts = {}
        for shift_id in shift_ids:
            shifts[shift_id] = self.update_shift_status(shift_id, 'active')

        return shifts

    def desactivate_shifts(self, shift_ids):
        shifts = {}
        for shift_id in shift_ids:
            shifts[shift_id] = self.update_shift_status(shift_id, 'inactive')

        return shifts

    def update_shift_status(self, shift_id, status):
        service_name = 'client'

        if status == 'active':
            function_name = 'shiftactivate'
        elif status == 'inactive':
            function_name = 'shiftdesactivate'

        params = {'id': shift_id, 'status': status}
        shift = call_function('PUT', service_name, function_name, params)

        print(shift)
        return shift.json()

    #UPDATE EMPLOYEES
    def add_employees_to_shift(self, employee_ids):
        for employee_id in employee_ids:
            self.add_employee_to_shift(employee_id)

    def remove_employees_from_shift(self, employee_ids):
        for employee_id in employee_ids:
            self.remove_employee_from_shift(employee_id)

    def add_employee_to_shift(self, employee_id):
        if not self.shift_id:
            return False
        params = {"employee_id": employee_id, "shift_id": self.shift_id, "status": ""}
        call_function('POST', 'client', 'addemployeetoshift', params)
        return True

    def remove_employee_from_shift(self, employee_id):
        if not self.shift_id:
            return False
        params = {"shift_id": self.shift_id, 'employee_id': employee_id}
        call_function('DELETE', 'client', 'removeemployeefromshift',params)
        return True

    #UPDATE MENU STATUS
    def activate_menu(self, menu_id):
        pass

    #GET CLIENTS
    def get_all_clients(self):
        service_name = 'client'
        function_name = 'clients'

        clients = call_function('GET', service_name, function_name)
        return clients.json()


class ClientAppJo():
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


if __name__ == "__main__":
    clientAPP = ClientApp(1)
    clientAPP.activate_shifts([1])
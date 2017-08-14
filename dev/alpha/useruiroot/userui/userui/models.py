from core.serializer.jsonable import Jsonable


class OrderLine:

    def __init__(self, item_id, quantity, price):
        self.item_id = item_id
        self.quantity = quantity
        # TODO price for checking ?
        self.price = price


@Jsonable('status', 'client_id', 'shift_id', 'menu_id', 'user_id', 'order_lines', 'ini_waiting_time')
class Order:

    def __init__(self, client_id, shift_id, menu_id, user_id, order_lines):
        self.status = 'created'
        self.client_id = client_id
        self.shift_id = shift_id
        self.menu_id = menu_id
        self.user_id = user_id
        self.order_lines = order_lines
        self.ini_waiting_time = 10 * len(self.order_lines)

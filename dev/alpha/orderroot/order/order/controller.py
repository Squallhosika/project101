
class OrderControl:

    @staticmethod
    def estimated_time(order):
        # TODO have to be implemented
        # TODO do we return timeSpan or double ???
        # timeSpan seems better but issue with database maybe
        return 5

    @staticmethod
    def queue_id(order):
        return order.shift_id

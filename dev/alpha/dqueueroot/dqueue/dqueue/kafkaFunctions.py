import order.order.kafkaInstance as ki
from core.kafka.KEvent import KEvent
from core.app.api.base import call_function
from dqueue.dqueue.apps import DqueueConfig
import json


def order_positioned_pending(body):
    raw_order = json.loads(body)

    # TODO look how to get time and rating
    body = {'masted_id': raw_order.shift_id,
            'type': 'pending',
            'id': raw_order.id,
            'time': 15,
            'rating': 4.5}

    order_in_request = call_function('POST', 'dqueue', 'createnode', json.dumps(body))
    kevent = KEvent(DqueueConfig().name, 'order', 'w', __name__, order_in_request.text)
    ki.kEventManager.kgenerator.publish(kevent)


def order_positioned_validated(body):
    raw_order = json.loads(body)
    # TODO look how to get time and rating
    body = {'masted_id': raw_order.shift_id,
            'type': 'validated',
            'id': raw_order.id,
            'time': 15,
            'rating': 4.5}
    body_json = json.dumps(body)

    call_function('DELETE', 'dqueue', 'deletenode', body_json)
    order_in_request = call_function('POST', 'dqueue', 'createnode', body_json)
    kevent = KEvent(DqueueConfig().name, 'order', 'w', __name__, order_in_request.text)
    ki.kEventManager.kgenerator.publish(kevent)

def order_remove_from_queue(body):
    call_function('DELETE', 'dqueue', 'deletenode', body)

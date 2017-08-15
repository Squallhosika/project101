import order.order.kafkaInstance as ki
from core.kafka.KEvent import KEvent
from core.app.api.base import call_function
from order.order.apps import OrderConfig
import json


def created_order(body):
    order_in_request = call_function('POST', 'order', 'createorder', body)
    kevent = KEvent(OrderConfig().name, 'order', 'w', __name__, order_in_request.text)
    ki.kEventManager.kgenerator.publish(kevent)


def validated_order(body):
    call_function('POST', 'order', 'ordervalidate', body)


def rejected_order(body):
    call_function('POST', 'order', 'orderreject', body)


def order_status_pickup_soon(body):
    body_deserialize = json.loads(body)
    body = {'id': body_deserialize.id, 'status': 'pickup_soon'}
    call_function('POST', 'order', 'orderstatus', body)


def order_status_to_pickup(body):
    body_deserialize = json.loads(body)
    body = {'id': body_deserialize.id, 'status': 'to_pickup'}
    call_function('POST', 'order', 'orderstatus', body)


def order_status_being_serve(body):
    body_deserialize = json.loads(body)
    body = {'id': body_deserialize.id, 'status': 'being_serve'}
    call_function('POST', 'order', 'orderstatus', body)


def order_status_completed(body):
    body_deserialize = json.loads(body)
    body = {'id': body_deserialize.id, 'status': 'completed'}
    call_function('POST', 'order', 'orderstatus', body)
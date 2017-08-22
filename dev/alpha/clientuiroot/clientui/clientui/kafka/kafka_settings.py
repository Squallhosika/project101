from . import kafkaFunctions as kf

BROKER = {
    'HOST': r'localhost',
    'PORT': r'9092',
    'TOPICS': [
        'order'
    ],
    'GROUPS': [
        'group-1'
    ]
}

TOPICS = {
    'order': '',
    '': '',
}


SERVICE_PARAMS = {
    'SENDER': r'clientui',
}


EVENT_TO_FCT = {
    'order': {
        'order_created': kf.notified_created_order,
        'order_positioned_pending': kf.notified_order_positioned_pending,
    }
}


FCT_TO_EVENT = {

}
#
#
# event_to_fct = \
#     {'order':
#          {'created_order': kf.notified_created_order,
#           'order_positioned_pending': kf.notified_order_positioned_pending,
#           'order_pickup_soon': lambda x: {},
#           'order_to_pickup': lambda x: {},
#           'arriving_for_pickup': lambda x: {}}
#      }
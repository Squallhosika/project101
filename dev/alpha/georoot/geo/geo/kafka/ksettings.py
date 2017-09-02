from . import kafkaFunctions as kf

BROKER = {
    'HOST': r'localhost',
    'PORT': r'9092',
    'TOPICS': [
        'test'
    ],
    'GROUPS': [
        'group-1'
    ]
}

TOPICS = {
    'test': '',
}


SERVICE_PARAMS = {
    'SENDER': r'clientui',
}


EVENT_TO_FCT = {
    'order': {
        'order_created': kf.notified_created_order,
        'order_positioned_pending': kf.notified_order_positioned_pending,
    },
    'test': {
        'test': kf.test,
    }
}


FCT_TO_EVENT = {
    kf.notified_created_order.__name__: {
        'sender':None,
        'broker_topic':None,
        'event_type':None,
        'event_name':'name',
        'body':None
    },
    kf.notified_order_positioned_pending.__name__: {
        'sender':None,
        'broker_topic':None,
        'event_type':None,
        'event_name':None,
        'body':None
    },
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
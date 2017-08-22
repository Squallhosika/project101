from core.kafka.KEventManager import KEventManager
from core.kafka.KSettings import KSettings
# import clientui.clientui.kafkaFunctions as kf


# event_to_fct = \
#     {'order':
#          {'created_order': kf.notified_created_order,
#           'order_positioned_pending': kf.notified_order_positioned_pending,
#           'order_pickup_soon': lambda x: {},
#           'order_to_pickup': lambda x: {},
#           'arriving_for_pickup': lambda x: {}}
#      }
#
# fct_to_event = \
#     {'order':
#          {'created_order': kf.notified_created_order,
#           'order_positioned_pending': kf.notified_order_positioned_pending,
#           'order_pickup_soon': lambda x: {},
#           'order_to_pickup': lambda x: {},
#           'arriving_for_pickup': lambda x: {}}
#      }
#
# host = 'localhost'
# port = '9092'
# topics = ['order']
# groups = ['group-1']
# sender = "userui"
# event_type = "w"



if __name__ == '__main__':
    # ksettings = KSettings('clientui') #event_to_fct, fct_to_event, host, port, topics, groups)
    kEventManager = KEventManager('clientui')
    kEventManager.publish('thisIsABody')
    # print(ksettings.BROKER['HOST'])
    # kEventManager = KEventManager(kSettings)
    # kEventManager.start()

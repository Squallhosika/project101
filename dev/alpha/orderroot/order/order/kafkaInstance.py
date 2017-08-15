from core.kafka.KEventManager import KEventManager
from core.kafka.KSettings import KSettings
import order.order.kafkaFunctions as kf


event_to_fct = \
    {'order':
         {'call_creation_order': kf.created_order,
          'validated_order': kf.validated_order,
          'rejected_order': kf.rejected_order,
          'order_pickup_soon': kf.order_status_pickup_soon,
          'order_to_pickup': kf.order_status_to_pickup,
          'being_serve': kf.order_status_being_serve,
          'order_completed': kf.order_status_completed},
     }

host = 'localhost'
port = '9092'
topics = ['order']
groups = ['group-1']
sender = "userui"
event_type = "w"

kSettings = KSettings(event_to_fct, host, port, topics, groups)
kEventManager = KEventManager(kSettings)

if __name__ == '__main__':
    kEventManager.start()
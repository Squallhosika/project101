from core.kafka.KEventManager import KEventManager
from core.kafka.KSettings import KSettings
import dqueue.dqueue.kafkaFunctions as kf


event_to_fct = \
    {'order':
         {'created_order': kf.order_positioned_pending,
          'validated_order': kf.order_positioned_validated,
          'rejected_order': kf.order_remove_from_queue,
          'order_completed': kf.order_remove_from_queue},
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

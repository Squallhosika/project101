from core.kafka.KEventManager import KEventManager
from core.kafka.KSettings import KSettings

event_to_fct = \
    {'order':
         {'create_order': lambda x: print("test0"),
          'delete_order': lambda x: print("test1")},
     'test':
         {'test0': lambda x: print("test2"),
          'test1': lambda x: print("test3")}
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
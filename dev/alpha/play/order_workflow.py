import os

from external.userApp import call_function
from play.utils import csv_to_req

# 1 user - get client around me
# 2 user - get menu of one client
# 3 user - create an order and post it
# 4 client - accept the order
# 5 user - check waiting time
# 6 client - ask next order
# 7 user - receive notification go to the bar
# 8 client - complete the order


### From the order service point of view

# 0 Initial set-up
input_dir = os.path.join(os.getcwd(), 'play', 'input')
csv_to_req(os.path.join(input_dir, 'order', 'items.csv'), 'POST', 'order', 'createitem')

# 1 Some clients pass online
call_function('POST', 'order', 'createqueue', {'client_id': 10})
call_function('POST', 'order', 'createqueue', {'client_id': 5})
call_function('POST', 'order', 'createqueue', {'client_id': 21})
call_function('POST', 'order', 'createqueue', {'client_id': 33})

# 2 users create orders and place it
order_ids = []
for i in range(1, 40):
    req = call_function('POST', 'order', 'createorder', {'user_id': i, 'client_id': 10})
    order_id = req.data['id']
    call_function('POST', 'order', 'orderadditem', {'item_id': 1, 'order_id': order_id, 'price': 2.5, 'quantity': 4})
    call_function('POST', 'order', 'orderadditem', {'item_id': 2, 'order_id': order_id, 'price': 4.5, 'quantity': 2})
    call_function('POST', 'order', 'orderadditem', {'item_id': 3, 'order_id': order_id, 'price': 9.5, 'quantity': 8})
    call_function('POST', 'order', 'placeorder', {'order_id': order_id})
    order_ids.append(order_id)

# 3 Client discover that order waiting for their acceptation.
#   two way to discover that:
#   - order sent by order service (Post request)
#   - client service check new need to approval every X second (Get request) -> choose here
# In the end the client accept most of the request

req_new_orders = call_function('GET', 'order', 'neworders', {'client_id': 10})
for order_id in order_ids[:3]: # replace order_ids by the req_new_orders parse (logic in client)
    call_function('POST', 'order', 'orderrejectedbyclient', {'order_id': order_id})

for order_id in order_ids[4:]: # replace order_ids by the req_new_orders parse (logic in client)
    call_function('POST', 'order', 'orderacceptedbyclient', {'order_id': order_id})
    req = call_function('GET', 'order', 'itemsbyorder', {'order_id': order_id})


req1 = call_function('POST', 'order', 'nexttoserve', {'client_id': 10, 'barman_id': 1})
req2 = call_function('POST', 'order', 'nexttoserve', {'client_id': 10, 'barman_id': 2})
call_function('POST', 'order', 'ordercompleted', {'order_id': req1.data['order_id']})

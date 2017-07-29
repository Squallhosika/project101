from dqueue.dqueue.models import *


class QueueControl:

    @staticmethod
    def add_node(queue, node_id, time, rating):
        new_last_node = None
        last_node_id = queue.node_id_last
        # queue is empty ?
        if last_node_id:
            new_last_node = Node.objects.Create(id=node_id, id_previous=None, id_next=None,
                                                queue=queue, time=time, rating=rating)
            queue.node_id_first = node_id
            queue.node_id_last = node_id
        else:
            old_last_node = Node.objects.get(id=last_node_id)
            new_last_node = Node.objects.Create(id=node_id, id_previous=last_node_id,
                                                id_next=None, queue=queue, time=time,
                                                rating=rating)
            old_last_node.id_next = node_id
            queue.node_id_last = node_id
            old_last_node.save()

        queue.save()
        return new_last_node

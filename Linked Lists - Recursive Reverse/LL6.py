class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head):
    linked_list = None
    cur = head

    while cur:
        next_node = cur.next
        cur.next = linked_list
        linked_list = cur
        cur = next_node

    return linked_list
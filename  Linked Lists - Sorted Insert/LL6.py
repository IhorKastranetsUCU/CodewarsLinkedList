class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    cur = head
    if data < cur.data:
        node_to_insert = Node(data)
        node_to_insert.next = cur
        return node_to_insert

    while cur.next:
        if cur.next.data > data:
            node_to_insert = Node(data)
            node_to_insert.next = cur.next
            cur.next = node_to_insert
            return head
        cur = cur.next
    return head
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node):
    slow = fast = node
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    res = 1
    cur = slow.next
    while cur != slow:
        res += 1
        cur = cur.next
    return res
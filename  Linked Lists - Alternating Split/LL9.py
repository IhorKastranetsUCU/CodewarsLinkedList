class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List must have at least two nodes")

    first = head
    second = head.next
    cur_first = first
    cur_second = second
    cur = head.next.next

    while cur:
        cur_first.next = cur
        cur_first = cur_first.next
        cur = cur.next
        if not cur:
            break
        cur_second.next = cur
        cur_second = cur_second.next
        cur = cur.next

    cur_first.next = None
    cur_second.next = None
    return Context(first, second)
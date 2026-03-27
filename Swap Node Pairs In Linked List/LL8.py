class Node(object):
    def __init__(self, next=None):
        self.next = next


def swap_pairs(head: Node):
    if not head or not head.next:
        return head
    cur = head
    head = cur.next

    while cur and cur.next:
        next_node = cur.next
        temp = next_node.next
        next_node.next = cur
        cur.next = temp
        if temp and temp.next:
            cur.next = temp.next
        cur = temp

    return head
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    unique_val = set()
    cur = head
    prev = None

    while cur:
        if cur.data in unique_val:
            prev.next = cur.next
        else:
            unique_val.add(cur.data)
            prev = cur
        cur = cur.next

    return head

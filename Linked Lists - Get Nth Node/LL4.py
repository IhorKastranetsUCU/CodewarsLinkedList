class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None or index < 0:
        raise IndexError

    cur = node
    for _ in range(index):
        cur = cur.next
        if cur is None:
            raise IndexError
    return cur
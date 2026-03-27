class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    linked_list = Node(data)
    linked_list.next = head
    return linked_list


def build_one_two_three():
    items = [1, 2, 3]
    head = Node(items[0])
    cur = head
    for node in items[1:]:
        cur.next = Node(node)
        cur = cur.next
    return head
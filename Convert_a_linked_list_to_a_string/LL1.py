class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    parts = []
    while node:
        parts.append(str(node.data))
        node = node.next
    return " -> ".join(parts + ["None"])
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        parts = []
        cur = self
        while cur:
            parts.append(str(cur.data))
            cur = cur.next
        return str(parts)


def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None

    parts = list_repr.split(" -> ")
    linked_list = Node(int(parts[0]))
    cur = linked_list
    for node in parts[1:]:
        if node == "None":
            break
        cur.next = Node(int(node))
        cur = cur.next
    return linked_list

print(linked_list_from_string("1 -> 2 -> 3 -> None -> None"))

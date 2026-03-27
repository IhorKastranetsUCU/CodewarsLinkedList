class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    new_node = source.data
    source = source.next
    cur_dest = Node(new_node)
    cur_dest.next = dest
    return Context(source, cur_dest)
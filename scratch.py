
class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def add_next( self, node ):
        self.next = node

    def add_data(self,data):
        self.data = data

    def next(self):
        return self.next

    def data(self):
        return self.data


class LinkedList():
    def __init__(self):
        self.start = None

    def get_last_node(self, node):
        if not node.next():
            return node
        return self.get_last_node(node.next())

    def collect_nodes(self, nodes, node):
        nodes.append(node.data())
        if node.next == None:
            return nodes

        return self.collect_nodes( nodes, node.next())

    def add_data(self, data):
        # hand data to node
        # if node is empty, store data there
        # if node is not empty, get next node
        new_node = Node(data)

        if self.start == None:
            self.start = new_node
            return

        last_node = self.get_last_node(self.start)

    def each(self, fn):


    print(self):






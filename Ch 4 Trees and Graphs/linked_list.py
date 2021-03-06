class LinkedList:
    def __init__(self, nodes=None):
        """ Initialize a linked list.

        :param nodes: a list of values representing each node in the linked list
        """
        self.head = None
        if nodes:
            node = Node(nodes.pop(0))
            self.head = node
            for value in nodes:
                node.next = Node(value)
                node = node.next

    # Traverse
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def get_head(self):
        return self.head

    def set_head(self, node):
        self.head = node

    def get_values(self):
        value_list = [elem.value for elem in self]
        return value_list

    def append_head(self, node):
        node.next = self.head
        self.head = node

    def get_tail(self):
        node = self.head
        while node.next:
            node = node.next
        return node

    def append_tail(self, llist):
        tail = self.get_tail()
        tail.next = llist.get_head()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
from reference.Node import Node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_to_front(self, data):
        if data is None:
            return data
        node = Node(data, next=self.head)
        self.head = node
        return node

    def append(self, data):
        if data is None:
            return data

        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        return node

    def get_all_data(self):
        data = []
        pointer = self.head
        while pointer is not None:
            data.append(pointer.data)
            pointer = pointer.next
        return data

    def find(self, data):
        pass
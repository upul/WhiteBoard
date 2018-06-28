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
        if self.head is None or data is None:
            return False
        current = self.head
        while current is not None:
            current_data = current.data
            if current_data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        if self.head is None or data is None:
            return False

        current = self.head
        if current.data == data:
            self.head = current.next
            return True

        while current.next is not None:
            if current.next.data == data:  # found it
                current.next = current.next.next
                return True
            current = current.next
        return False

    # Chapter 2 Q 1 Part 1
    # TODO: (upul) actually we don't need two pointers.
    def remove_duplicate(self):
        if self.head is None:
            return False

        indicator = set()
        ptr_prev = self.head
        indicator.add(ptr_prev.data)

        flag = False
        ptr_current = self.head.next
        while ptr_current is not None:
            data = ptr_current.data
            if data not in indicator:
                indicator.add(data)
                ptr_prev = ptr_current
                ptr_current = ptr_current.next
            else:
                ptr_prev.next = ptr_current.next
                ptr_current = ptr_current.next
                flag = True
        return flag

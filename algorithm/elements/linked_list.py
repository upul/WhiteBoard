class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) if self.data else None


def search(L, key):
    while L and L.data != key:
        L = L.next
    return L


def to_list(L):
    result = []
    while L:
        result.append(L.data)
        L = L.next
    return result

def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    node.next = node.next.next 


if __name__ == '__main__':
    a1 = ListNode(1)
    a2 = ListNode(2, a1)
    a3 = ListNode(3, a2)
    head = ListNode(4, a3)

    print(to_list(head))
    print(search(head, 20))

    insert_after(a3, ListNode(111))
    print(to_list(head))
    print(search(head, 111))

    delete_after(a3)
    print(to_list(head))

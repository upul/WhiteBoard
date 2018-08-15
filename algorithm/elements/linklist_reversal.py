class ListNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def reversal_stack(tree):
    current = tree
    dummy = ListNode()

    while current:
        next_node = current.next

        current.next = dummy.next
        dummy.next = current

        current = next_node
    return dummy.next


def to_list(tree):
    list = []
    current = tree
    while current:
        list.append(current.data)
        current = current.next
    return list


if __name__ == '__main__':
    a1 = ListNode(10)
    a2 = ListNode(20, a1)
    root = ListNode(30, a2)

    print(to_list(root))
    reverse = reversal_stack(root)
    print(to_list(reverse))

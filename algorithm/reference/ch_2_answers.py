from LinkedList import LinkedList


class LinkedListQ3(LinkedList):

    def delete_middle(self, node):
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next


ll = LinkedListQ3()
n0 = ll.append('A')
n1 = ll.append('B')
n2 = ll.append('C')
ll.delete_middle(n2)
print(ll.get_all_data())

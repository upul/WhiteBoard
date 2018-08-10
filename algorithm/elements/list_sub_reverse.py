class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def reverse_subset(L, start, end):
    dummy_head = prev = tail = Node()
    counter = 1

    while L:
        if counter == start -1:
            while counter <= end:
                L = L.next
                tail.next = L
                L.next = L 
        


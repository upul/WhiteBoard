from LinkedList import LinkedList


class DeleteK(LinkedList):

    def delete_k(self, n):
        num_forward = self.size() - n
        counter = 1
        current = self.head
        while counter is not None:
            if counter == num_forward:
                break
            counter += 1
            current = current.next
        if current.next is None:
            self.head = self.head.next
        else:
            current.next = current.next.next


if __name__ == '__main__':
    ll = DeleteK()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    assert ll.size() == 5
    print(ll.get_all_data())
    ll.delete_k(5)
    print(ll.get_all_data())

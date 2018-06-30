from LinkedList import LinkedList


class LinkedListQ6(LinkedList):
    def is_palindrome(self):
        if self.size() <= 1:
            return False

        reverse = []
        current = self.head
        while current is not None:
            reverse.append(current.data)
            current = current.next

        current = self.head
        while current is not None:
            if current.data != reverse.pop():
                return False
            current = current.next
        return True

    def is_palindrome_2(self):
        if self.size() <= 1:
            return False

        half = self.size() // 2

        first_half_data = []
        current = self.head
        i = 0
        while i < half:
            first_half_data.append(current.data)
            current = current.next
            i += 1

        if self.size()% 2 == 1:
            current = current.next

        while current is not None:
            if current.data != first_half_data.pop():
                return False
            current = current.next
        return True


if __name__ == '__main__':
    ll = LinkedListQ6()
    ll.append('a')
    ll.append('b')
    ll.append('a')
    assert ll.is_palindrome_2() == True

    ll = LinkedListQ6()
    ll.append('a')
    ll.append('b')
    ll.append('c')
    assert ll.is_palindrome_2() == False

    ll = LinkedListQ6()
    assert ll.is_palindrome_2() == False

    ll = LinkedListQ6()
    ll.append('a')
    assert ll.is_palindrome_2() == False

    ll = LinkedListQ6()
    ll.append('1')
    ll.append('2')
    ll.append('3')
    ll.append('2')
    ll.append('1')
    assert ll.is_palindrome_2() == True

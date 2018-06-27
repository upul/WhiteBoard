import unittest

from reference.LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_insert_to_front(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.get_all_data(), [])

        linked_list.insert_to_front('A')
        self.assertEqual(linked_list.get_all_data(), ['A'])

        linked_list.insert_to_front('B')
        linked_list.insert_to_front('C')
        self.assertEqual(linked_list.get_all_data(), ['C', 'B', 'A'])

    def test_append(self):
        linked_list = LinkedList()

        linked_list.append('A')
        self.assertEqual(linked_list.get_all_data(), ['A'])

        linked_list.append('B')
        linked_list.append('C')
        self.assertEqual(linked_list.get_all_data(), ['A', 'B', 'C'])


if __name__ == '__main__':
    unittest.main()

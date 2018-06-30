import unittest

from reference.LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_size(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.size(), 0)

        linked_list.append('A')
        self.assertEqual(linked_list.size(), 1)

        linked_list.append('A')
        linked_list.append('B')
        linked_list.append('A')
        self.assertEqual(linked_list.size(), 4)


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

    def test_find(self):
        linked_list = LinkedList()

        linked_list.append('A')
        self.assertEqual(linked_list.find('A'), True)
        self.assertEqual(linked_list.find('C'), False)

        linked_list.append('B')
        linked_list.append('C')
        linked_list.append('D')
        linked_list.append('E')
        self.assertEqual(linked_list.find('B'), True)
        self.assertEqual(linked_list.find('D'), True)
        self.assertEqual(linked_list.find('E'), True)
        self.assertEqual(linked_list.find('Z'), False)

    def test_delete(self):
        linked_list = LinkedList()
        linked_list.append('A')
        self.assertEqual(linked_list.delete('A'), True)

        linked_list = LinkedList()
        linked_list.append('A')
        linked_list.append('B')
        linked_list.append('C')
        self.assertEqual(linked_list.delete('B'), True)
        self.assertTrue(linked_list.delete('C'))
        self.assertFalse(linked_list.delete('C'))
        self.assertTrue(linked_list.delete('A'))
        self.assertFalse(linked_list.delete('D'))

        self.assertEqual(linked_list.get_all_data(), [])

    def test_delete_duplicates(self):
        linked_list = LinkedList()
        linked_list.append('A')
        linked_list.remove_duplicate()
        self.assertEqual(linked_list.get_all_data(), ['A'])

        linked_list = LinkedList()
        linked_list.append('A')
        linked_list.append('A')
        linked_list.remove_duplicate()
        self.assertEqual(linked_list.get_all_data(), ['A'])

        linked_list = LinkedList()
        linked_list.append('A')
        linked_list.append('A')
        linked_list.append('B')
        linked_list.append('C')
        linked_list.append('D')
        linked_list.append('D')
        linked_list.append('D')
        linked_list.append('A')
        linked_list.remove_duplicate()
        self.assertEqual(linked_list.get_all_data(), ['A', 'B', 'C', 'D'])

        linked_list = LinkedList()
        linked_list.remove_duplicate()
        self.assertEqual(linked_list.get_all_data(), [])


if __name__ == '__main__':
    unittest.main()

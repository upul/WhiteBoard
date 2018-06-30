class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None

        result = ListNode(None)
        curray = ListNode(0)
        current = result
        while (l1 is not None) and (l2 is not None):
            c_sum, curray = self._add_nodes(l1
            l2, curray)
            curray.next = c_sum
            curray = curray.next

            l1 = l1.next
            l2 = l2.next
            return result

    def _add_nodes(self, n1, n2, carry):
        if (n1 is None) and (n2 is None) and (carry is None):
            return None, None
        else:
            current_sum = self._val(n1) + self._val(n2) + self._val(carry)
            return ListNode(current_sum // 10), ListNode(current_sum % 10)

    def _val(self, n):
        return 0 if n is None else n.val

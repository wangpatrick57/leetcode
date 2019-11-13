# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr_node_l1 = l1
        curr_node_l2 = l2

        while True:
            self._add_num(curr_node_l1, curr_node_l2.val)

            if curr_node_l2.next == None:
                return l1

            curr_node_l2 = curr_node_l2.next

            if curr_node_l1.next == None:
                break

            curr_node_l1 = curr_node_l1.next

        while curr_node_l2 != None:
            curr_node_l1.next = ListNode(curr_node_l2.val)

            curr_node_l1 = curr_node_l1.next
            curr_node_l2 = curr_node_l2.next

        return l1

    def _add_num(self, l, num):
        """
        :type l: ListNode
        :type num: int
        :rtype: None
        """
        this_sum = l.val + num
        l.val = (this_sum) % 10

        if this_sum >= 10:
            if l.next != None:
                self._add_num(l.next, 1)
            else:
                l.next = ListNode(1)

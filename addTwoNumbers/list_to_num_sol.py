# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''returns the linked list representing the sum of two linked list numbers'''
        return self._num_to_list(self._list_to_num(l1) + self._list_to_num(l2))

    def _list_to_num(self, l: ListNode) -> int:
        '''converts a linked list to an integer'''
        curr_node = l
        curr_val = curr_node.val
        num = 0
        ten_power = 0

        while curr_node != None:
            curr_val = curr_node.val
            num = curr_val * pow(10, ten_power) + num
            ten_power += 1
            curr_node = curr_node.next

        return num

    def _num_to_list(self, num: int) -> ListNode:
        '''converts an integer to a linked_list'''
        first_node = ListNode(num % 10)
        prev_node = first_node
        num = num // 10

        while num > 0:
            node = ListNode(num % 10)
            prev_node.next = node
            prev_node = node
            num = num // 10

        return first_node

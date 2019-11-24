# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr_node = head
        nodes = list()

        while curr_node != None:
            nodes.append(curr_node)
            curr_node = curr_node.next

        index = len(nodes) - n

        if index == 0:
            head = nodes[1]
        else:
            nodes[index - 1].next = nodes[index].next

        return head

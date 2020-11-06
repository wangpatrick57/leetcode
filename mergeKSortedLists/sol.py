# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_ll(node: ListNode) -> None:
    if node == None:
        print('None')
        return

    curr_node = node

    while curr_node.next != None:
        print(f'{curr_node.val} -> ', end='')
        curr_node = curr_node.next

    print(curr_node.val)

def llfl(l: ['val']) -> ListNode:
    if l == None:
        return None

    if len(l) == 0:
        return None

    ret_node = ListNode(l[0])
    curr_node = ret_node

    for val in l[1:]:
        curr_node.next = ListNode(val)
        curr_node = curr_node.next

    return ret_node

from collections import deque

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        if lists == None or len(lists) == 0:
            return None

        q = deque()

        for node in lists:
            q.append(node)

        while len(q) >= 2:
            q.append(self._merge2lists(q.popleft(), q.popleft()))

        return q.popleft()

    def _merge2lists(self, list_a: ListNode, list_b: ListNode) -> ListNode:
        if list_a == None and list_b == None:
            return None
        elif list_a == None:
            return list_b
        elif list_b == None:
            return list_a
        else:
            if list_a.val <= list_b.val:
                ret_node = list_a
                next_a = list_a.next
                next_b = list_b
            else:
                ret_node = list_b
                next_a = list_a
                next_b = list_b.next

        curr_node = ret_node

        while next_a != None and next_b != None:
            if next_a.val <= next_b.val:
                curr_node.next = next_a
                next_a = next_a.next
            else:
                curr_node.next = next_b
                next_b = next_b.next

            curr_node = curr_node.next

        if next_a != None:
            curr_node.next = next_a
        else:
            curr_node.next = next_b

        return ret_node

sol = Solution()
print_ll(sol._merge2lists(None, None))
print_ll(sol.mergeKLists(None))

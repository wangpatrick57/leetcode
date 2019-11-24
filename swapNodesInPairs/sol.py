DEBUG = True

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr_node = head
        new_head = head
        prev_node = head
        old_node = None
        i = 0

        while curr_node != None:
            print(curr_node.val)
            next_node = curr_node.next

            if i % 2 == 1:
                if i == 1:
                    new_head = curr_node

                if old_node != None:
                    old_node.next = curr_node

                prev_node.next = curr_node.next
                curr_node.next = prev_node
                old_node = prev_node

            prev_node = curr_node
            curr_node = next_node
            i += 1

        return new_head

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        head = ListNode(1)
        curr_node = head

        for i in range(2, 5):
            new_node = ListNode(i)
            curr_node.next = new_node
            curr_node = new_node

        curr_node = sol.swapPairs(head)

        while curr_node != None:
            print(curr_node.val, end = '')
            curr_node = curr_node.next

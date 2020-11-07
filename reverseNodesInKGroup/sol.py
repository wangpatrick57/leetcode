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

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = 0
        last_first = None
        this_first = None
        curr_node = head
        prev_node = None
        new_head = None

        while curr_node != None:
            next_node = curr_node.next

            if n % k == 0:
                last_first = this_first
                this_first = curr_node
                n = 0
            else:
                if n % k == k - 1:
                    if last_first != None:
                        last_first.next = curr_node

                    if new_head == None:
                        new_head = curr_node

                curr_node.next = prev_node

            n += 1
            prev_node = curr_node
            curr_node = next_node

        if n == k:
            this_first.next = None
        else:
            # send correct node to point to end section
            if last_first != None:
                last_first.next = this_first

            # unreverse end section
            start_node = prev_node
            curr_node = start_node
            prev_node = None

            for _ in range(n):
                next_node = curr_node.next

                if prev_node != None:
                    curr_node.next = prev_node

                prev_node = curr_node
                curr_node = next_node

            start_node.next = None

        return new_head or head

sol = Solution()
print_ll(sol.reverseKGroup(llfl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 4))

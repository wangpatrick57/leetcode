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

class Solution:
    def mergeKLists(self, lists):
        # base case
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        # divide
        mid = (len(lists) + 1) // 2
        l1 = self.mergeKLists(lists[:mid])
        l2 = self.mergeKLists(lists[mid:])

        # conquer
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1

        if l1.val < l2.val:
            head = l1
            burner = l2
        else:
            head = l2
            burner = l1

        hopper = head

        while hopper != None and burner != None:
            hopper_next = hopper.next

            if hopper_next == None or hopper_next.val > burner.val:
                hopper.next = burner
                hopper = burner
                burner = hopper_next
            else:
                hopper = hopper_next

        return head

if __name__ == '__main__':
    s = Solution()
    print(s.mergeKLists([]), 'None')
    print(s.mergeKLists([None]), 'None')
    print()
    ll = s.mergeKLists([ListNode(1, ListNode(3)), ListNode(2)])
    print_ll(ll)
    print('1 -> 2 -> 3')
    print()
    ll = s.mergeKLists([ListNode(1, ListNode(2)), ListNode(3)])
    print_ll(ll)
    print('1 -> 2 -> 3')
    print()
    ll = s.mergeKLists([ListNode(1, ListNode(2, ListNode(3))), None])
    print_ll(ll)
    print('1 -> 2 -> 3')
    print()
    ll = s.mergeKLists([None, ListNode(1, ListNode(2, ListNode(3)))])
    print_ll(ll)
    print('1 -> 2 -> 3')
    print()
    ll = s.mergeKLists([ListNode(2), ListNode(1, ListNode(2, ListNode(3)))])
    print_ll(ll)
    print('1 -> 2 -> 2 -> 3')
    print()
    ll = s.mergeKLists([ListNode(2), ListNode(1, ListNode(2, ListNode(3))), ListNode(0, ListNode(4, ListNode(8))), ListNode(3, ListNode(5))])
    print_ll(ll)
    print('0 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 5 -> 8')
    print()

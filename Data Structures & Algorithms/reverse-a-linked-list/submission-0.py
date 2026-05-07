# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        prev_el = head
        el = head.next
        head.next = None

        while el is not None:

            next_el = el.next
            el.next = prev_el
            prev_el = el
            el = next_el

        return prev_el
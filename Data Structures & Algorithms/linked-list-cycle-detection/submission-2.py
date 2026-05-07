# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
        
    #     seen = set()

    #     nxt = head

    #     while nxt:

    #         print(seen)
    #         if nxt in seen:
    #             return True
    #         seen.add(nxt)
    #         nxt = nxt.next

    #     return False

    # 2-pointer O(1) extra space instead of O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False

        
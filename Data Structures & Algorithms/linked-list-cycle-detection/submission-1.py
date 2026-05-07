# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen = set()

        nxt = head

        while nxt:

            print(seen)
            if nxt in seen:
                return True
            seen.add(nxt)
            nxt = nxt.next

        return False

        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val > list2.val:
            head = list2
            next1 = list1
            next2 = list2.next
        else:
            head = list1
            next1 = list1.next
            next2 = list2

        curr = head

        while next1 or next2:

            if not next1:
                nextx = next2
                curr.next = nextx
                curr = nextx
                next2 = next2.next
            elif not next2:
                nextx = next1
                curr.next = nextx
                curr = nextx
                next1 = next1.next
            elif next1.val > next2.val:
                nextx = next2
                curr.next = nextx
                curr = nextx
                next2 = next2.next
            else:
                nextx = next1
                curr.next = nextx
                curr = nextx
                next1 = next1.next

        return head



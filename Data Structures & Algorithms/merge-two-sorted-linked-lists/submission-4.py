# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val:
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
                curr.next = next2
                return head
            elif not next2:
                curr.next = next1
                return head
            elif next1.val > next2.val:
                curr.next = next2
                curr = next2
                next2 = next2.next
            else:
                curr.next = next1
                curr = next1
                next1 = next1.next

        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        if head is None:
            return None

        temp = curr.next
        while curr is not None:
            curr.next = prev
            prev = curr 
            curr = temp
            if temp is not None:
                temp = temp.next

        return prev
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 
        if head is None:
            return
        
        temp = head
        while temp is not None:
            length+=1
            temp = temp.next
        
        target = length - n

        prev = None
        curr = head
        tar_count = 0
        while curr is not None:
            if tar_count == target and prev is not None:
                prev.next = curr.next
                curr.next = None
                return head
            elif tar_count == target and prev is None:
                prev = curr
                curr = curr.next
                prev.next = None
                return curr
            else:
                tar_count+=1
                prev = curr
                curr = curr.next
        
        return head
        


        
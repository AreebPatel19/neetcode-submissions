# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set1 = set()
        curr1 = head
        curr2 = head
        while curr1 != None:
            curr1 = curr1.next
            curr2 = curr2.next
            if curr2 == None:
                return False
            curr2 = curr2.next

            if curr2 == None:
                return False
            if curr1.val == curr2.val:
                return True
        return False
        


        
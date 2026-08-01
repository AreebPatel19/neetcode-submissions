# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        len=0
        while curr != None:
            curr = curr.next
            len +=1
        pos = len - n
        curr = head
        prev = head
        temp = head
        if pos == 0:
            head = head.next
        elif pos == len-1:
            curr = head
            count = 0
            prev = head
            while curr.next != None:
                prev = curr
                curr = curr.next
                count+=1
            prev.next = None
        else:
            curr = head
            count = 0
            prev = head
            while count !=pos:
                prev = curr
                curr = curr.next
                count+=1
            prev.next = curr.next
        return head
        
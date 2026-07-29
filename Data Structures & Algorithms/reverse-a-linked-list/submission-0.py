# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        list1=[]
        while curr !=None:
            list1.append(curr.val)
            curr=curr.next
        print(list1)
        i=len(list1) -1
        curr = head
        while i>=0:
            curr.val = list1[i]
            curr = curr.next
            i-=1 
        return head


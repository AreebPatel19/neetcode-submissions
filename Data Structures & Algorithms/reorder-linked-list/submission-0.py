# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack1 = []
        tail = head
        curr = head
        curr2 = head
        count = 0
        while tail != None:
            stack1.append(tail)
            count+=1
            tail = tail.next
        count = count // 2
        while count:
            tail1 = stack1.pop()
            #print(tail1.val)
            temp = curr.next
            curr.next = tail1
            tail1.next = temp
            curr = tail1
            curr = curr.next
            count-=1
        curr.next = None
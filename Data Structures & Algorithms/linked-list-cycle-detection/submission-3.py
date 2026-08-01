class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # As long as fast and the node after fast exist
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            # If they meet, they are trapped in a cycle
            if slow == fast:
                return True
                
        # If the loop finishes, fast hit the end of the list
        return False
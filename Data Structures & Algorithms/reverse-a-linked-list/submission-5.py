class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None:
            nxt = curr.next     # 1. Save the next node so we don't lose it
            curr.next = prev    # 2. Reverse the pointer of the current node
            prev = curr         # 3. Step the 'prev' pointer forward
            curr = nxt          # 4. Step the 'curr' pointer forward
            
        # At the end, 'curr' is None and 'prev' is the new head of the list
        return prev
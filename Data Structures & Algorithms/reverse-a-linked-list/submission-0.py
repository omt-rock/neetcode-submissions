class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        l.reverse()

        dummy = ListNode(0)
        curr = dummy
        for i in l:
            curr.next = ListNode(i)
            curr = curr.next
           
        return dummy.next
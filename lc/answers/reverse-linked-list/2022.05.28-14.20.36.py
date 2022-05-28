class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        dummy = ListNode(val=0, next=head)
        curr = head
        while curr.next:
            X = curr.next
            curr.next = X.next
            X.next = dummy.next
            dummy.next = X
        return dummy.next
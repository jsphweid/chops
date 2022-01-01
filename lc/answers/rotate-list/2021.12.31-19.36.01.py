"""

"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        list_length = self.get_len(head)
        k %= list_length

        # make an infinite loop
        self.make_infinite(head)

        # traverse k-1 times
        curr = head
        for _ in range(list_length - k):
            curr = curr.next
        res = curr
        
        # break loop
        for _ in range(list_length - 1):
            curr = curr.next
        curr.next = None
        return res

    def make_infinite(self, head: ListNode):
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = head


    def get_len(self, head: ListNode) -> int:
        res, curr = 0, head
        while curr:
            curr = curr.next
            res += 1
        return res
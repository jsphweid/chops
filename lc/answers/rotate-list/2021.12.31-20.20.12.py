# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        queue = deque([])
        while head:
            queue.append(head.val)
            head = head.next
        k %= len(queue)
        for _ in range(k):
            queue.appendleft(queue.pop())
        res = ListNode(queue.popleft(), None)
        curr = res
        for _ in range(len(queue)):
            curr.next = ListNode(queue.popleft(), None)
            curr = curr.next
        return res
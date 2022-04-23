"""
=== Brute Force Approach ===
solve using a stack... then we can think about how to only use a linked list

~~Complexity Analysis
Time - O(n)
Space - O(n)

I remembered solving it from the end, which is why I had to put it all in a list first.
But you can solve these problems from the beginning, but you have to keep a tuple in
the stack, not just a number (so you can update the position also). When you solve it
from the beginning, you have to write a lot less code!
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        items, stack, res = [], [], []
        while head:
            items.append(head.val)
            head = head.next
        for num in items[::-1]:
            if stack and num < stack[-1]:
                res.append(stack[-1])
                stack.append(num)
            else:
                while stack and num >= stack[-1]:
                    stack.pop()
                res.append(stack[-1] if stack else 0)
                stack.append(num)
        res.reverse()
        return res

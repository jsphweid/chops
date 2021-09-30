"""
===== Initial Thoughts =====
two pass is simple (O(2n)/O(n))... traverse once to get the items in list form, then 1 to check for palindrome

how could we do it in 1 pass though without a second pointer?

I'm not sure today. I think I'll just two a basic two pass approach for now...

=== Implemented Approach ===
one pass to get as a list
then do two pointer palindrome checker

~~Complexity Analysis
Time - O(2n)
Space - O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True

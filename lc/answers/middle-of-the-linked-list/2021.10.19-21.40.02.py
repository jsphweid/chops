"""
===== Initial Thoughts =====
I think using two pointers here is the strat. We'll just have one that moves twice as slowly...

edge cases... (I'm guessing)
[1] -> [1]
[1, 2] -> [2]
[1, 2, 3] -> [2, 3]

=== Implemented Approach ===
have two pointers point to the top.
Have a while loop that goes through the whole linked list
keep track of how many we've moved through. When that number is odd/even, increment the other pointer
by 1. When we reach the end of the linked list, the slower pointer should be returned...

We really just need to work out exactly how the middle pointer moves...
Save we move on odd moves
1 2 3 4 5
e o e o e (even/odd)

so by the end we'll have had two odds... which means 1->2->3.. we correctly end on node 3

what about for even length linked lists?
1 2 3 4 5 6
e o e o e o
we'll have moved 3 times,... so node 4... this is also correct

what about for edge case?
1 - shouldn't move
1 2 - should be 2
1 2 3 - should also be 2

I think this really works out

~~Complexity Analysis
Time - O(n) - single pass traversal... can't really do better than that
Space - O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        middle = head
        i = 0
        while current.next:
            current = current.next
            if i & 1:
                middle = middle.next
            i += 1 
        return middle.next if i & 1 else middle

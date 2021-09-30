"""
===== Initial Thoughts =====
somehow I don't immediately remember the solution to this but what a bizarre problem

I'm not sure where to begin.

The problem is obviously we don't have an explicit reference to the previous node (i.e. doubley linked list).

We could just have it assume the identity of the next one...? That sounds vaguely familiar. The next one would
have to assume the ID of the next and so on.

So in 4->5->1->9
deleting 5 means turning 5 into 1, but also turning 1 into 9 and turning 9 into None
5node.val becomes 1. go to next
1node.val becomes 9. go to next
9node becomes None... but it's too late since we lost a reference

We need to start earlier.

5node.val becomes 1. 5node (now 1node) points to next.next (which is 9), advance
still not clear

4-5-1-9
change current
4-1-1-9
next.next is 9 so advance to second 1
change current
4-1-9-9
next.next is None, so we're stopping there
4-1-9-None
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while True:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None
                return
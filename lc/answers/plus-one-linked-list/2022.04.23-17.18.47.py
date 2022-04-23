# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
4 -> 2 -> 3
recurse(4)
    recurse(2)
        recurse(3)

recurse(0) -> 1
    recurse(0) -> 1
"""

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def recurse(node):
            remainder = recurse(node.next) if node.next else None
            if remainder or not node.next:
                if node.val == 9:
                    node.val = 0
                    return 1
                node.val += 1

        return ListNode(1, head) if recurse(head) else head
        
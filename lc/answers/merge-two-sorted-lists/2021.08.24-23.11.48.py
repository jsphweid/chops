"""
It's easy because they are already sorted.

I think the simple approach is making a pointer for each list
and advancing them strategically.

Not sure why the args are Optional...? Oh because they are not lists, but
list nodes...

The drawing makes it a bit unclear as to which node comes first
when there is a tie... Maybe it doesn't matter? The first time it happens
the second list comes first. The second time, it's the first. For this first
attempt, I'll assume the order doesn't matter.

Can there be two nodes with the same value in a single list?

Another way we could possibly do this is by using one of the existing lists
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # copy args to variables
        l1_node = l1
        l2_node = l2
        base_node = None
        true_base_node = None

        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # if not l1 or not l2:
        #     return None

        # make a while loop that can continue looping while either l1 or l2 is truthy
        while l1_node or l2_node:
            if l1_node:
                if l2_node:
                    if l1_node.val < l2_node.val:
                        if base_node:
                            base_node.next = l1_node
                            base_node = base_node.next
                        else:
                            base_node = l1_node
                            true_base_node = l1_node
                        l1_node = l1_node.next
                    else:
                        if base_node:
                            base_node.next = l2_node
                            base_node = base_node.next
                        else:
                            base_node = l2_node
                            true_base_node = l2_node
                        l2_node = l2_node.next
                else:
                    if base_node:
                        base_node.next = l1_node
                        base_node = base_node.next
                    else:
                        base_node = l1_node
                        true_base_node = l1_node
                    l1_node = l1_node.next

            if l2_node:
                if l1_node:
                    if l2_node.val < l1_node.val:
                        if base_node:
                            base_node.next = l2_node
                            base_node = base_node.next
                        else:
                            base_node = l2_node
                            true_base_node = l2_node
                        l2_node = l2_node.next
                    else:
                        if base_node:
                            base_node.next = l1_node
                            base_node = base_node.next
                        else:
                            base_node = l1_node
                            true_base_node = l1_node
                        l1_node = l1_node.next
                else:
                    if base_node:
                        base_node.next = l2_node
                        base_node = base_node.next
                    else:
                        base_node = l2_node
                        true_base_node = l2_node
                    l2_node = l2_node.next
            
        return true_base_node

# TODO: redo this... I was not thinking clearly at all but somehow managed to get it after a few tries.
# 1. How can we do the base assignment better?
# 2. There's a ton of duplication with `if base_node:`... how can we remove that???
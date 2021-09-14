"""
I'm going to build this using iteration... I think it can be done pretty simply by using
a queue... We will add the root node, then add each child. Actually that's already wrong since
the order we want to process this is we want to move onto grandchildren before we process the
next child... That doesn't appear to fit a queue.

Maybe a stack can be used somehow. My first impression is that this doesn't really work. Say
we'd process 1, then add 3, 2, 4. The next to get processed would be the one at the top of the stack
which is 4. But we really need to process 3 next.

It's like we need a queue, but then we need the ability to add stuff at the beginning, not the end.
We could iterate backwards over the list. But that's a stack. 

What about a backwards iteration using a stack!
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        results = []        
        stack = [root]
        while len(stack):
            node = stack.pop()
            results.append(node.val)
            for c in node.children[::-1]:
                stack.append(c)
        return results
        
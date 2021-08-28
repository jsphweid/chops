"""
This should be relatively easy considering previous problems I have done.

Will we use the max() function which takes a list of nums? We could transform each path/route
into a number. I'm not very confident with that exercise yet though.

We could easily use something like we did from the top-down `symmetric-tree` approach but instead
of having a queue that keeps getting bigger, we could just store the last depth-increment?

Could we answer this recursively? My intuition on whether a recursive solution could work or not
is whether we "use" or "use the definition" of the function at every node in the tree and it 
still makes sense. Also state variables like in `path-sum` make it pretty obvious when it can be
used.

Here the "definition" aspect seems to make sense; at every node, we can define the maxDepth as
maybe the current_depth + maxDepth() of a child node? TODO: I need to think about this more, but
it seems like we can't use this because there is no state variable in the function definition that
can store the current depth....

Let's use a queue...
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Container:
    def __init__(self, node: Optional[TreeNode], depth: int):
        self.node = node
        self.depth = depth

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [Container(root, 1)]
        max_depth = 1
        while len(queue):
            container = queue.pop(0)
            node = container.node
            if node:
                max_depth = max([max_depth, container.depth])
                nextDepth = container.depth + 1
                queue.extend([Container(node.left, nextDepth), Container(node.right, nextDepth)])
        return max_depth

    """
    failed the first time... let's walk through everything again
    submitted twice more, once pushing he max_depth = 1, then again
    the initial root node with a depth of 1. This is because after reviewing
    the examples on leetcode, it seems they count from a 1-index instad
    of 0-index. But if there is nothing, it's 0.

    I loooked online `0 / 39 test cases passed.`

    Noticed I had `root` instead of `node` in a crucial part... damn... maybe shouldn't
    have ordered a triple... double would've been better...

    Still failed. Still none passed. wtf. It's gotta be something dumb.

    I honestly have no idea why it's failing.... it's probably something obvious
    but i can't see it. I'll look at it in the morning. I don't want to start
    printing junk out because that's too easy. I'm trying to take the slow road
    here.

    So I uncommented "TreeNode" defintiion and it succeeded. Then I commented it
    back out and it succeeded. I think it's just a case of "forgot to save"... i.e.
    it should have worked when I switched `root` -> `node` above. Chalking this
    off as a dumb mistake.
    """


"""
Still can't help but feel there is a better solution for all these types of problems.
Will revisit again someday.
"""
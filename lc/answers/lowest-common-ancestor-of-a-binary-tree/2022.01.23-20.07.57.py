"""
===== Initial Thoughts =====
since vals are unique we could get the path of every node and find which num 
they have in common then using some mapping of nums to node, we could return the node

but that seems like it takes up lots of space.

what if we could DFS and flatten the nodes somehow so that 
children eventually make theirselves toward the top. Then when the two
nodes in question meet, that is the result.

I swear I've solved some easy version of this and it wasn't that hard. But now I'm struggling
probably because I haven't worked with binary trees in a while.

After thinking a while, not sure I have another choice but to do it the heavy memory way if I want 
to finish in 15 minutes...

UPDATE: So I did that for 10 minutes and then gave up because that idea is dumb.
Honestly maybe it's union find or BFS is better...?
BFS seems wrong because in anything other than a simple example where they are both on the same row it
just doesn't seem beneficial.

UF seems like what I was talking about above but isn't UF destructure in that you forget immediate
parents? Hmm.. only if you compress it...

30 minutes up.

Looking at discussions... I was just over-complicating this.

The problem is I didn't really think about how it can be solved recursively using the original function.

One insight that is interesting here is that once you find at least one, you can just return it... 
It doesn't even matter that it may have a child that was the other one. You're still only interested
in the one closest to the root anyways.

Also, I just didn't think returning None for child calls or anywhere was a proper response
because the problem always has a solution. This is a silly concern as in the grand scheme of things
a value will always be returned so returning None within the local scope of a child context is fine.
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in [None, p, q]: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


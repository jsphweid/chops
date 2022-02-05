"""
===== Initial Thoughts =====
first thought is... how does this compare to inorder?

[3,9,8,4,0,1,7,null,null,null,2,5]
inorder = [4 9 0 2 3 5 1 8 7]
res = [[4],[9,5],[3,0,1],[8,2],[7]]

That's probably not the best direction.

Actually this isn't so bad to get the vertical slices. It's just... how many ".left" or ".right" has it gone over.
That determines the bucket it goes in. Ordering within that bucket might be a bit tricky though.

For example, the 0 and 1. 
0 is left-right
1 is right-left
so since l > r, we could just encode the path as "lr" and "rl" and sort lexicographically?
Actually... l < r... but it means a sort will put it first.

So llr and lrl still goes to llr.

trace
stack=[]
d={
    -2: [(4,"ll")]
    -1:[(9, "l"), (5,"rll")]
    0: [(3, ""),(0, "lr"),(1,"rl")]
    1: [(8, "r"),(2, "lrr")]
    2: [(7,"rr")]
}
[[4], [9,5], [3,0,1]] etc. should work

failed on [1,2,3,4,5,6,null,null,7,8,null,null,9,null,10,null,11,10]
[null,10,null,11,10]
it was because of a goof.

I bet we could go faster if we just had things in the right order in the first place.
We probably just need to use a queue. DONE. And yes, it's faster.
"""
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        deck, d = deque([(root, 0, "")]), defaultdict(list)
        while deck:
            node, h_shift, path = deck.popleft()
            d[h_shift].append((node.val, path))
            if node.left:
                deck.append((node.left, h_shift - 1, path + "l"))
            if node.right:
                deck.append((node.right, h_shift + 1, path + "r"))
        res = []
        for shift in sorted(list(d.keys())):
            res.append([a[0] for a in sorted(d[shift], key=lambda v: len(v[1]))])
        return res



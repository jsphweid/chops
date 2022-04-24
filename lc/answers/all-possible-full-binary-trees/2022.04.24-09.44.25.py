"""
===== Initial Thoughts =====
7... subtract either 1 or 3... keep ones that end in 0
6, 4
5 3, 3 1
4 2, 2 0, 2 0, 0 -2
3 1, 1 -1, 1 -1, 0

but that only gives me the count... also that will have duplicates
let's pause that thought.

from the top node, unless n=1, there has to be 2 children
if n=2, result has to be []

Wow, this is surprisingly tough to think about.
Even if we recurse and come up with different children, the top level
node will be the same. So how do we make separate unique trees?

9 -> 
7 -> 5 trees
6 -> 0 trees
5 -> 2 trees(1-2,3-4,5)
4 -> 0 trees
3 -> 1 tree (1-2,3)
2 -> 0 trees
1 -> 1 tree (1)

if number is even, there has to be 0 trees, right?

with each number 2 greater, it's like adding 2 nodes on some leaf.
but then removing the duplicates. I still don't understand the 
mechanism of how to do this.

It seems to me since they all need to be unique TreeNodes, we have
to understand the structure of each unique tree first and then generate
the trees by creating a top root node. 

Let's understand it layer by layer for n=7
1 2 2 2
1 2 2 2
1 2 4
1 2 2 2
1 2 2 2
That doesn't describe shape enough?

n=5 => 1 2 2, 1 2 2
n=3 => 1 2
n=1 => 1

This problem has a very high acceptance rate. So I'm a little confused
as to why it seems so difficult to me.

Why can't we just generate all possibilities and then remove duplicates?
We need some way to serialize structures.

I have to look at the answers -- I've wasted too much time

I feel less bad after looking at the solutions. I wouldn't have ever
gotten this one. Some people took issue with the cloning trees concern.

One of the things I think I could've noticed is that the nodes 'could'
be seen as being labeled 1-N. Then I could've seen the pattern of nodes
with even numbers have 2 children while odd nodes are leaves. I could've
gotten a little further.

allPossibleFBT(5)
    2
        left=allPossibleFBT(1) -> [TreeNode(0)]
        right=allPossibleFBT(3)
            2
                left=allPossibleFBT(1) -> [TreeNode(0)]
                right=allPossibleFBT(1) -> [TreeNode(0)]

I mostly copied the answer. Didn't really understand what I was copying.

Let's try to understand it a little more.

{
    0: [], 
    1: [TreeNode(0)]
}

recurse(5) -> [...]
    recurse(0) -> []
    recurse(1) -> [TreeNode(0)]
    recurse(2) -> []
        recurse(0) -> []
        recurse(1) -> [TreeNode(0)]
            (r) recurse(0) -> []
    recurse(3) l=
        recurse(0) -> []
        recurse(1) -> [TreeNode(0)]
            (r) recurse(0)
        recurse(2) -> [] (from cache)
    recurse(4)

this is too much for me now...
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        self.memo = {0: [], 1: [TreeNode(0)]}
        self.recurse(n)
        return self.memo[n]

    def recurse(self, n: int):
        if n not in self.memo:
            res = []
            for l in range(n):
                # we can have l nodes on left and r nodes on right
                r = n - 1 - l

                for left in self.recurse(l):
                    for right in self.recurse(r):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        res.append(node)
            self.memo[n] = res
        return self.memo[n]


        
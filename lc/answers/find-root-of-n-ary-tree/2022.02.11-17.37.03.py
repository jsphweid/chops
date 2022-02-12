"""
===== Initial Thoughts =====
easy thing would be to scan over each node once, writing children vals to a set
then iterate over once more checking to see if the value is in the set.
The one that isn't in the set is the result

=== Brute Force Approach ===

~~Complexity Analysis
Time - O(n)
Space - O(n)

Easy two pass
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        seen = set()
        for node in tree:
            for child in node.children:
                seen.add(child.val)
        for node in tree:
            if node.val not in seen:
                return node

=== Implemented Approach ===
for the "no memory" constraint... what if we eliminated all grandchildren and below for each node.
when we iterate over again, the only one that should have any children is the root...

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        def remove_all_but_direct_children(node):
            if node.children:
                for child in node.children:
                    remove_all_but_direct_children(child)
                    child.children = []
        for node in tree:
            remove_all_but_direct_children(node)
        for node in tree:
            if node.children:
                return node

it doesn't work though because it's destructive

another idea -- find height of every subtree and keep the longest. This is constant space 
but not constant time unless we cache ones we've seen (which would make it not linear space)

since it seems like the numbers are 1 TO N, what if we sorted the list with 1 pass
[5,2,3,1,4] becomes
[1,2,3,4,5] through swapping

Hmm... I don't think that can be done in one-pass though.
[3,1,6,2,7,4,5] index 0
[6,1,3,2,7,4,5] index 0
[4,1,3,2,7,6,5] index 0
[2,1,3,4,7,6,5] index 0
[1,2,3,4,7,6,5] index 1
[1,2,3,4,7,6,5] index 2
[1,2,3,4,7,6,5] index 3
[1,2,3,4,5,6,7] index 4
[1,2,3,4,5,6,7] index 5
[1,2,3,4,5,6,7] index 6
It's 7 swaps BUT more than 7 cycles.
So it's not linear.

BUT if we had them in order, then we could use that as a state. Maybe let's do it anyway.

[3,1,6,2,7,4,5]
val=3
i+1 => 1
tree[0] = 6

[5, 4, 3, 6, 2, 1]
i=0 i+1=1
----
0th=4

Actually this doesn't work because the vals can be like [5, 1, 3]

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        for i in range(len(tree)):
            while tree[i].val != i + 1:
                v = tree[i].val - 1
                tree[i], tree[v] = tree[v], tree[i]
        for i, node in enumerate(tree):
            if node:
                for child in node.children:
                    tree[child.val - 1] = None
        for node in tree:
            if node:
                return node

OK, I read the discussions and it's pretty interesting what the actual solution is. Just subtract the sum
of all children from the sum of all parents. That will yield the parent node...

"""
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        parents, childs = 0, 0
        for node in tree:
            parents += node.val
            childs += sum([c.val for c in node.children])
        diff = parents - childs
        for node in tree:
            if node.val == diff:
                return node

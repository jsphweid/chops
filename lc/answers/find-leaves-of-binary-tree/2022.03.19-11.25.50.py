"""
===== Initial Thoughts =====
I've solved this before but don't immediately remember how. The brute force would be to get all
the leaves and detach them, re-running until the root no longer exists. But that is wasteful since
we are traversing the same nodes over and over again.

How about we build an adjacency list using sets.

Their Example 1: looks like [1,2,3,4,5] and should produce [[4,5,3],[2],[1]]
adj list looks like
1: {2,3}
2: {4,5}
3: {}
4: {}
5: {}

The process is to remove all empty sets, keeping track of which ones are being deleted.
So we eliminate 3,4,5
we are left with:
1: {2,3}
2: {4,5}

we then remove 3 from the 1's set
remove 4 and 5 from the 2's set

1: {2}
2: {}

so we eliminate 2

we then remove 2 from the 1's set
1: {}
so we eliminate 1

We can use a reverse lookup to more quickly locate the sets we should delete
I'm taking a chance because I'm assuming the numbers are unique.

OK after failures because of "memory limit", it seems making that assumption was a horrible idea.
How can I recover this using this solution? One way would be to make the numbers unique by making everything
a string and add the path on there

~~Complexity Analysis
Time - 
Space - 

adj={1: {2,3}, 2: {}}
child_to_parent={4:2, 5:2, 2:1, 3:1}
to_delete={4,5
res=[[4,5,3]]
"""
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        adj, child_to_parent, to_delete = {}, {}, set()
        def traverse(parent, path=""):
            parent_val = f"{str(parent.val)}_{path}"
            adj[parent_val] = set()
            to_delete.add(parent_val)
            for child, char in [(parent.left, "l"), (parent.right, "r")]:
                if child:
                    child_val = f"{str(child.val)}_{path}{char}"
                    if parent_val in to_delete: to_delete.remove(parent_val)
                    child_to_parent[child_val] = parent_val
                    adj[parent_val].add(child_val)
                    traverse(child, path + char)
        traverse(root)
        res = []
        while adj:
            nxt_to_delete = set()
            res.append([])
            for item in to_delete:
                res[-1].append(int(item.split("_")[0]))
                del adj[item]
                if item in child_to_parent:
                    parent = child_to_parent[item]
                    adj[parent].remove(item)
                    if not adj[parent]:
                        nxt_to_delete.add(parent)
            to_delete = nxt_to_delete
        return res

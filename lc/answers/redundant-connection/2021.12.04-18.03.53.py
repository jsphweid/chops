"""
=== Brute Force Approach ===
one way to consider it is:
if we started from the right edge and built a 
graph minus that edge, would we touch every node.

~~Complexity Analysis
Time - O(n^2)
Space - O(n)

=== Implemented Approach ===
what if we built the network slowly and every time we find a useless edge (an edge
in which both start and end have already been found), we update the reundant edge

ACTUALLY THIS DOESN'T WORK... FAILS ON:
[[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]

My definition of a "useless" edge is incorrect. It doesn't work because an edge
joining two nodes from different groups is not redundant even if both nodes
have already been used in edge relationships before. I think I made this same mistake
before. 

I think a union find is the correct method here. Since we're not given the number
of nodes, we have to assume length 1001 nodes in our lookup. If we find an edge
where both nodes have the same parent, then it's redundant.

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        lookup, res = list(range(1001)), None

        def find(node):
            while lookup[node] != node:
                node = lookup[node]
            return node
        
        def union(node1, node2):
            a, b = find(node1), find(node2)
            if a == b:
                nonlocal res
                res = [node1, node2]
            else:
                lookup[a] = b

        for start, end in edges:
            union(start, end)
        return res

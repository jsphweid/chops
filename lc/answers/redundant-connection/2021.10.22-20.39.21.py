"""
===== Initial Thoughts =====
I think it removing the extra is removing something that WON'T abandon a node. This means
we could do one pass to get all the nodes and counts. Then offer up one that has redundant connections
and keep overwriting it with a newer answer and return whatever is last
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        ret = None
        for l, r in edges:
            counts[l] += 1
            counts[r] += 1
        for l, r in edges:
            if counts[l] > 1 and counts[r] > 1:
                ret = [l, r]
        return ret

ERROR
That didn't work because of `[[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]`
just because something is mentioned twice doesn't mean that it's connected to something that _would_
be stranded if it disappeared...

Maybe we can try more of a simpler / brute force approach. 

Like if we deleted one at a time, could we figure out if there were no connections?
For example, when mine broke in the above, it broke on [6,8]. This isn't a valid redundant connection
because deleting it strands 2. That's pretty easy to recognize afterwards because 2 (and 6) have only
a one count afterwards... But this seems to fall apart quickly because 2/6 could be connect to other 
now separated nodes.

What we really want to know is, if we deleted a node, is there still a way to get back to it?
for example, in [[1,2],[1,3],[2,3]], for each
is there another way to get from 1->2 except 1->2
is there another way to get from 1->3 except 1->3
is there another way to get from 2->3 except 2->3
the answer is yes in each, so we take the last.

Really the trick here is having an efficient way to see if we can "get to there". We have to build
some sort of graph.
{
    1:[3],
    2:[3],
    3:[1,2]
}

{
    1:[3],
    2:[1,3],
    3:[1,2]
}
[[1,2],[2,3],[3,4],[1,4],[1,5]]
{
    1: {2,4,5},
    2: {1,3},
    3: {2,4},
    4: {3,1},
    5: {1}
}
[[1,3],[3,4],[1,5],[3,5],[2,3]]
{
    1: {3,5},
    2: {3},
    3: {1,2,4,5},
    4: {3},
    5: {1,3}
}
"""
from collections import defaultdict
import copy
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def has_connection(graph, start, end, explored, ignore):
            if end in graph[start]:
                if (start, end) != ignore and (end, start) != ignore:
                    return True
            for node in graph[start]:
                if start == ignore[0] and node == ignore[1]: continue
                if start == ignore[1] and node == ignore[0]: continue
                if node not in explored and has_connection(graph, node, end, explored.union({node}), ignore):
                    return True
            return False
        graph = defaultdict(set)
        for l, r in edges:
            graph[l].add(r)
            graph[r].add(l)

        redundant = None
        for l, r in edges:
            if has_connection(graph, l, r, {l}, (l, r)):
                redundant = [l, r]
        return redundant

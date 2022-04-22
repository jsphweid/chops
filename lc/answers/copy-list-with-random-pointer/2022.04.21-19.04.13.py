"""

Came up with this

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        d = {}
        curr = head
        while curr:
            d[curr.val] = {
                "node": Node(curr.val),
                "next": curr.next.val if curr.next else None,
                "random": curr.random.val if curr.random else None}
            curr = curr.next
        res = d[head.val]["node"]
        curr = res
        while curr:
            nxt_val, rand_val = d[curr.val]["next"], d[curr.val]["random"]
            curr.next = d[nxt_val]["node"] if nxt_val is not None else None
            curr.random = d[rand_val]["node"] if rand_val is not None else None
            curr = curr.next
        return res

But then it failed because there can be duplicate numbers... Oops.
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
{7: "node": node, "random": val or null, "next": val or null}
 000      111    222    333    444
[[7,null],[13,0],[11,4],[10,2],[1,0]]
lookup = {}
nodes = [Node(7, None),]

"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        nodes, lookup = [], {}
        curr = head
        while curr:
            lookup[id(curr)] = len(nodes)
            nodes.append(Node(curr.val, random=curr.random))
            curr = curr.next
        res = nodes[0]
        for i in range(len(nodes)):
            curr = nodes[i]
            curr.next = nodes[i + 1] if i != len(nodes) - 1 else None
            curr.random = nodes[lookup[id(curr.random)]] if curr.random is not None else None
        return res

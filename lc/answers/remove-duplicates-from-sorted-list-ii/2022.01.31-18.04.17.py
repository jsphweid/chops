"""
===== Initial Thoughts =====
1-2-2-3-4-4

probably store the first instance of a number...
for example 1
then go to next. It's different... update it
now we store 2.
Go to next, it's another 2. Continue
It's 3. That's different. tie first two to 3. Store 3.
Continue. etc.
Get to None, we have 4. Tie 4 to None and return

~~Complexity Analysis
Time - O(n)
Space - O(1)

1-2-3-4-4
curr=None stored=4

Oh wait... I totally misunderstood the question. We're supposed to remove duplicates all together, even the original.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        res, curr, stored = head, head, None
        while curr:
            if stored:
                if stored.val != curr.val:
                    stored.next = curr
                    stored = curr
            else:
                stored = curr
            curr = curr.next
        stored.next = None
        return res

This works well to delete dupes but it keeps at least 1. That is incorrect.

Easy way that uses too much memory and is two pass is to go through list, put all singles in another list.
Then join those together. Let's try.

from collections import deque
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        while head:
            if head.val in d:
                count, node = d[head.val]
                d[head.val] = (count + 1, node)
            else:
                d[head.val] = (1, head)
            head = head.next

        deck = deque([])
        for num in sorted(list(d.keys())):
            count, node = d[num]
            if count == 1:
                node.next = None
                deck.append(node)

        if not deck:
            return None

        head = deck.popleft()
        curr = head
        while deck:
            curr.next = deck.popleft()
            curr = curr.next
        return head

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
2-3-3-4-5-5
last_good=2-4 curr=5 res=2 bad=5

1-1-1-2-3
last_good=2-3 curr=3 res=2 bad=1

1-1

1-2-2
last_good=1 curr=1 res=c bad=None
"""

from collections import deque
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_good, curr, res, bad = None, head, None, None
        while curr:
            if curr.val != bad:
                if curr.next and curr.val == curr.next.val:
                    bad = curr.val
                    if last_good:
                        last_good.next = None
                else:
                    if last_good:
                        last_good.next = curr
                    last_good = curr
                    res = curr if res == None else res
            curr = curr.next
        return res



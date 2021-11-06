"""

[5, 2, 3, 8, 6, 3]
n = 2

i=1
i=2 curr=2 lag=5 curr=3
i=3 curr=3 lag=2 curr=8
i=4 curr=8 lag=3 curr=6
i=5 curr=6 lag=8 curr=3


[1,2]
n=1
i=0
i=1, curr=1 lag=1 curr=2


[1]
n=1

i=1 curr


while node.next

[1,2,3,4,5]
2

i=0 
curr=1 i=1 lag=None curr=2
curr=2 i=2 lag=1 curr=3
curr=3 i=3 lag=2 curr=4
curr=4 i=4 lag=3 curr=5

[1,2]
2

i=0 
curr=1 i=1 curr=2

[1,2]
2

[1,2,3]
3

curr=1 i=1 lag=None curr=2
curr=2 i=2 lag=None curr=3


lag=1

[5]
i=0 lag=None curr=5



"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        lag = None
        i = 0
        while curr.next:
            i += 1
            if lag:
                lag = lag.next
            else:
                if i == n:
                    lag = head
            curr = curr.next
        if not lag: 
            if (i + 1) == n:
                return head.next
            else:
                lag = head
        lag.next = lag.next.next
        return head
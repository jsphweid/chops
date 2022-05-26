"""
dummy -> None
         1 -> 1 -> None
                   curr
list1 = []
list2 = [3,4]
node = 
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            node = None
            if list1.val <= list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            node.next = None
            curr.next = node
            curr = curr.next

        curr.next = list1 if list1 is not None else list2

        return dummy.next
        
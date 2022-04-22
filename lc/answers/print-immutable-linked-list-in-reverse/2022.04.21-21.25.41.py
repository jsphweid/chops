# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

"""
1->2->3->4->None
printLinkedListInReverse(1)
    printLinkedListInReverse(2)
        printLinkedListInReverse(3)
            printLinkedListInReverse(4) -> print and return None

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        nxt = head.getNext()
        if nxt is not None:
            self.printLinkedListInReverse(nxt)
        head.printValue()

"""

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        nxt = head.getNext()
        if nxt is not None:
            self.printLinkedListInReverse(nxt)
        head.printValue()
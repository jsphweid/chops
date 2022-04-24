# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
import random
# 1 2 3 4 5 6 7 8 9 10
# 1 4 7 10

"""
failed on 10, 1, 10, 20, 100
length = 5
bins = [10 node, 10 node, 100 node]
bin_size = 2
div, rem = 2, 1
num bins = 3
last bin size = 1

10 - 1 - 10 - 20 - 100
"""
class Solution:
    def __init__(self, head: Optional[ListNode]):
        length = self._get_length(head)
        self.bins = []
        self.bin_size = int(math.sqrt(length))
        div, rem = divmod(length, self.bin_size)
        self.num_bins = div + (rem > 0)
        self.last_bin_size = self.bin_size if rem == 0 else rem
        for _ in range(self.num_bins):
            self.bins.append(head)
            for __ in range(self.bin_size):
                if not head: break
                head = head.next

    def _get_length(self, head):
        curr = head
        res = 0
        while curr:
            res += 1
            curr = curr.next
        return res

    def getRandom(self) -> int:
        bin_index = random.randint(0, self.num_bins - 1)
        bin_size = self.last_bin_size if bin_index + 1 == self.num_bins else self.bin_size
        node = self.bins[bin_index]
        for _ in range(random.randint(0, bin_size - 1)):
            node = node.next
        return node.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
from math import inf
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one_index, closest = None, inf
        for i, num in enumerate(nums):
            if num == 1:
                if prev_one_index != None:
                    closest = min(i - prev_one_index - 1, closest)
                prev_one_index = i
        return closest >= k
"""
aaron and i spent a lot of time on this but did it in the web browser

"""

from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        positions = defaultdict(list)
        lengths = defaultdict(int)
        for i, num in enumerate(nums):
            positions[num].append(i)
            lengths[num] += 1

        record = max(lengths.values())
        checked = set()

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if diff == 0: continue
                if (nums[j], nums[i]) in checked:
                    continue
                checked.add((nums[j], nums[i]))
                next_num = nums[j] + diff
                largest = 2
                lowest_index = j
                while True:
                    found_one = False
                    for idx in positions[next_num]:
                        if idx > lowest_index:
                            largest += 1
                            next_num += diff
                            lowest_index = idx
                            found_one = True
                            break
                    if not found_one: break
                record = max(largest, record)
        return record        
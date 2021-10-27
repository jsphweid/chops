from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        positions = defaultdict(set)
        res = set()
        for i in range(len(nums)): positions[nums[i]].add(i)
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    missing = target - (nums[i] + nums[j] + nums[k])
                    if missing in positions:
                        pos = positions[missing]
                        if len(pos - {i, j, k}) > 0:
                            res.add(tuple(sorted([nums[i], nums[j], nums[k], missing])))
        return [list(item) for item in res]


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        closest = sum(nums[:3])
        closest_diff = abs(target - closest)
        for i in range(N - 2):
            j, k = i + 1, N - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                diff = abs(s - target)
                if diff < closest_diff:
                    closest = s
                    closest_diff = diff
                if s < target: j += 1
                else: k -= 1
        return closest


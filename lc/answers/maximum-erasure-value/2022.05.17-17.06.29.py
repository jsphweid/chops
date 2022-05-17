class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        curr = best = j =0
        for i, num in enumerate(nums):
            if num in seen:
                while num in seen:
                    seen.remove(nums[j])
                    curr -= nums[j]
                    j += 1

            curr += num
            seen.add(num)
            best = max(best, curr)
        return best

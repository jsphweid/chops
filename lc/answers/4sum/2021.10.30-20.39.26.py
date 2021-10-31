class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        N = len(nums)
        for i in range(N - 3):
            for j in range(i + 1, N - 2):
                k, l = j + 1, N - 1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s < target: k += 1
                    elif s > target: l -= 1
                    else:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
                        k += 1
                        l -= 1
        return [list(r) for r in res]
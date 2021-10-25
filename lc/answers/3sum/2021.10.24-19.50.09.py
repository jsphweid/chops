"""
===== Initial Thoughts =====


=== Brute Force Approach ===
do what we do in two sum with brute force...?

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        done = set()
        res = []
        def serialize(arr):
            return ",".join(map(str, sorted(arr)))
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        arr = [nums[i], nums[j], nums[k]]
                        serialized = serialize(arr)
                        if serialized not in done:
                            res.append(arr)
                            done.add(serialized)
        return res

~~Complexity Analysis
Time - O(n^3) but also
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        done = set()
        res = []
        def serialize(arr):
            return ",".join(map(str, sorted(arr)))
        indexed = {num: i for i, num in enumerate(nums)}
        for i in range(len(nums) - 1):
            if nums[i] > 0: break
            for j in range(i + 1, len(nums)):
                comp = (nums[i] + nums[j]) * -1
                if comp in indexed and indexed[comp] != i and indexed[comp] != j:
                    ans = [nums[i], nums[j], nums[indexed[comp]]]
                    serialized = serialize(ans)
                    if serialized not in done:
                        res.append(ans)
                        done.add(serialized)                    
        return res
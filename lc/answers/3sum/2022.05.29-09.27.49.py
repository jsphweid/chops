"""
===== Initial Thoughts =====
[-1,0,1,2,-1,-4]
 -1 

=== Brute Force Approach ===
3 for loops

~~Complexity Analysis
Time - O(n^3)

=== Implemented Approach ===
just do a 2 sum approach to save a loop

~~Complexity Analysis
Time - O(n^2)
Space - O(n)

[-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        if N < 3: return []
        sums = set()
        seen = {nums[0]}
        for i in range(1, N - 1):
            for j in range(i + 1, N):
                compliment = (nums[i] + nums[j]) * -1
                if compliment in seen:
                    sums.add((compliment, nums[i], nums[j]))
            seen.add(nums[i])
        return [list(s) for s in sums]

read a solution I really liked and was EASY to understand
what I didn't do good enough was remove duplicates in num space
I only did it at the end which is more expensive
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, z, p = [],[],[]
        for num in nums:
            if num == 0:
                z.append(0)
            elif num < 0:
                n.append(num)
            else:
                p.append(num)
        N, P = set(n), set(p)
        res = set()

        if len(z) >= 3:
            res.add((0,0,0))

        if len(z) > 0:
            for num in p:
                if -num in n:
                    res.add((-num,0,num))

        for i in range(len(n) - 1):
            for j in range(i + 1, len(n)):
                compliment = -(n[i] + n[j])
                if compliment in P:
                    res.add(tuple(sorted([n[i], n[j], compliment])))

        for i in range(len(p) - 1):
            for j in range(i + 1, len(p)):
                compliment = -(p[i] + p[j])
                if compliment in N:
                    res.add(tuple(sorted([compliment, p[i], p[j]])))
        return res

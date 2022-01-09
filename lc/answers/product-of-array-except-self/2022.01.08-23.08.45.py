"""
apparently I've solved this problem before but I don't remember it.

Obviously without the `You must write an algorithm that runs in O(n) time and without 
using the division operation.` constraint it's trivial...

I just can't think of a way to do it otherwise though...

read through everything
I understand the intuition.
funny thing was that I almost had understood it before looking 
at discussion but just didn't quite connect all the dots
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        one, two, curr_one, curr_two = [0] * N, [0] * N, 1, 1
        for i in range(N):
            curr_one *= nums[i]
            one[i] = curr_one
            curr_two *= nums[N - 1 - i]
            two[N - 1 - i] = curr_two
        res = []
        for i in range(N):
            if 0 < i < N-1:
                res.append(one[i-1] * two[i+1])
            elif i == 0:
                res.append(two[i+1])
            else:
                res.append(one[i-1])
        return res

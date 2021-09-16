"""
this question seems kind of dumb. They phrased it a certain way but the args don't represent 
the problem at all... It should be easy enough...

failed it once, I didn't read the problem clearly enough... Good job leetcode, you win
My simple solution failed on
[2,2] -> [2,1]... not [2,3]

Reading instructions more.
[number_that_occurs_twice, number_thats_missing]

honestly we should just start at 1, once there is a mismatch we know a problem has occured
and even there we know what the duplicate is...

failed it again, again, didn't understand 100% of the nuances of the problem until an edge case happened
`[3,2,2]` -> `[2,1]` not `[3,1]
I incorrectly assumed that the number that occurs twice was the one that's missing.
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_missing = None
        num_twice = None
        all_nums = set(nums)
        already_processed = set()
        for i, num in enumerate(nums):
            if (i + 1) not in all_nums:
                num_missing = i + 1
            if num in already_processed:
                num_twice = num
            already_processed.add(num)
        return [num_twice, num_missing]
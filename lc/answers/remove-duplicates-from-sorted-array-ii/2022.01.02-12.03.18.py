"""
===== Initial Thoughts =====
[0,0,1,1,1,1,2,3,3]

2
[0,0,1,1,1,1,2,3,3]

5
[0,0,1,1,2,2,3,3,4,4,1,3,2,4,4]


[0,0,1,1,2,1,2,2,2,3,3,3,4,4,4]
i=6 insert_i=5

failed because apparently they do want you to cut off the last items in python... that's stupid

oh actually I misread... we're supposed to return the number of non-dupes
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_i = 0
        for i, curr in enumerate(nums):
            if i < 2:
                insert_i += 1
            else:
                num_at_capacity = curr == nums[insert_i - 1] and curr == nums[insert_i - 2]
                if not num_at_capacity:
                    nums[insert_i] = curr
                    insert_i += 1
        return insert_i



            







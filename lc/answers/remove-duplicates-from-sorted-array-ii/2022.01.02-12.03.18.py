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
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_i, dupes = 0, 0
        for i, curr in enumerate(nums):
            if i < 2:
                insert_i += 1
            else:
                if curr == nums[insert_i - 1] and curr == nums[insert_i - 2]:
                    dupes += 1
                else:
                    nums[insert_i] = curr
                    insert_i += 1
        for _ in range(dupes):
            nums.pop()



            







class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = nums[0]
        max_num_index = 0
        valid = True
        for i in range(1, len(nums)):
            num = nums[i]
            # if we encounter a new max
            if num > max_num:
                # for it to be valid, it has to be twice has high at least as the last 
                valid = (num >= (2 * max_num))
                max_num = num
                max_num_index = i
            else:
                # we may get back to invalid if a near max number happens
                if num * 2 > max_num:
                    valid = False
        return max_num_index if valid else -1

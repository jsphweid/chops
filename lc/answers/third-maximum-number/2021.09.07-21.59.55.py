class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        if len(unique_nums) < 3:
            return max(unique_nums)

        top_three = unique_nums[0:3]

        for num in unique_nums[3:]:
            # find min
            current_lowest_value = min(top_three)

            # if num is greater than that min
            if num > current_lowest_value:
                # find index and replace it
                i = top_three.index(current_lowest_value)
                top_three[i] = num


        return min(top_three)
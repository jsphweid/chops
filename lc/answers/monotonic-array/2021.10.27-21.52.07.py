class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if asc == False:
                    return False
                elif asc == None:
                    asc = True
            elif nums[i] < nums[i - 1]:
                if asc == True:
                    return False
                elif asc == None:
                    asc = False
        return True

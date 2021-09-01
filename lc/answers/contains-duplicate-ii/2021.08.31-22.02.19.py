"""
        if len(nums) <= 1:
            return False

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and j - i <= k:
                    return True
        return False

my original solution didn't work because of timeouts

time to use a hashmap

{
    1: [0, 3]
    2: [1]
    3: [2]
}

{
    1: [0, 2, 3]
    0: [1]
}

{
    1: [0, 3]
    2: [1, 4]
    3: [2, 5]
}
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # iterate once over nums building a map of value -> List[indices]
        mapping = {}
        for i, val in enumerate(nums):
            if val in mapping:
                mapping[val].append(i)
            else:
                mapping[val] = [i]

        # iterate over values of map we built
        for indices in mapping.values():
            if len(indices) > 1:
                # check to see if any of the distances between the values <= k
                for i in range(1, len(indices)):
                    if indices[i] - indices[i - 1] <= k:
                        return True

        return False





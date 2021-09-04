"""
The idea here is to use a hashmap in order to save the inner iteration.

Only one valid answer exists and you can't use the same element twice. This doesn't necessarily imply that two numbers in the array can't be the same... or does it? Duplicate numbers != Duplicate indices. So I think it _can_ exist. Like [1, 2, 2, 4, 6]. In the target == 4, we could say the 
answer is indices [1, 2] (which are both 2). Actually I don't know why I'm thinking this hard
about it because Example 3 lists this exact scenario.

My original thought was to have a map of value to index. Then when we run into a value, we check to see if the complimentary value exists in the dictionary. But if there are collisions... Actually, it
just occurred to me that this is impossible because in the case like the one above, we'd have a map that only consisted of {1:0, 2:1} when we got to the third index (which is also 2). If can't collide on a irrelevant index because such a presence would violent the constraints of the question "Only one valid answer exists"

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums):
            compliment_value = target - num
            if compliment_value in mapping:
                compliment_index = mapping[compliment_value]
                return [compliment_index, i]
            mapping[num] = i

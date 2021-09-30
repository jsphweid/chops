"""
=== Brute Force Approach ===
iterate over each num in inclusive ranges. if num not in list, add to another list. summarize ranges of that other list

~~Complexity Analysis
Time - O(upper-lower * n) n is length list (assumes list search)
Space - O(upper-lower)

=== Implemented Approach ===
The better idea is to iterate only through nums, not the entire range. But that means that lower/upper have to be a part
of the range...

it makes things easy when we add them on the ends, adding 1 to the right and subtracting 1 on the left

~~Complexity Analysis
Time - O(n) n is length of nums
Space - O(n)
"""

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        all_nums = [lower - 1] + nums + [upper + 1]
        result = []
        for i in range(1, len(all_nums)):
            if abs(all_nums[i] - all_nums[i - 1]) > 1:
                left = all_nums[i - 1] + 1
                right = all_nums[i] - 1
                result.append(str(left) if left == right else f"{left}->{right}")
        return result
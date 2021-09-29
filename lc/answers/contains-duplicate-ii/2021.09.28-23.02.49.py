"""
===== Initial Thoughts =====
let's brute force this

=== Brute Force Approach ===
iterate over list with two for loops. if we find a matching value, check to see if their indicies are 

~~Complexity Analysis
Time - O(n**2)
Space - O(1)


nevermind.. that times out

```
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if j - i <= k:
                        return True
        return False
```
"""

from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        organized = defaultdict(list)
        for i, num in enumerate(nums):
            organized[num].append(i)
        for indicies in organized.values():
            if len(indicies) > 1:
                for i in range(1, len(indicies)):
                    if (indicies[i] - indicies[i - 1]) <= k:
                        return True
        return False

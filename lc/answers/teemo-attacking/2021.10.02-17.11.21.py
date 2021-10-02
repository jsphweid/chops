"""
===== Initial Thoughts =====


=== Brute Force Approach ===
have a set, for each num in time series, add new items to set
timeSeries = [1,2], duration = 2
for 1, add [1, 2]
for 2, add [2, 3]
set contains {1, 2, 3}, length 3

~~Complexity Analysis
Time - O(len(timeSeries) * duration)
Space - O(len(timeSeries) * duration)

let's see if brute force works

IT DOES NOT

=== Implemented Approach ===
return duration if len is 1
a better approach would be to keep a count
start on 1st index. The choose the minimum number between the diff
of the last and the duration (max poison duration). then add the max to the end

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i in range(1, len(timeSeries)):
            total += min(duration, timeSeries[i] - timeSeries[i - 1])
        return total + duration
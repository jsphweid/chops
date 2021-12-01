"""
===== Initial Thoughts =====
this can be solved through simulation and _maybe_ by insight...

=== Brute Force Approach ===
simulation... basically reproduce the rules over and over again until we have an unchanged list
Since the input is relatively constrained, then it shouldn't be too horrible

~~Complexity Analysis
hard to say here, but rough guess, if everything leans inward and the most it can be is 1-100
then worst case will be 50 array passes? But that's constant time...  :suggestive-eyebrows
Time - constant
Space - constant

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

tracing
[6,2,3,4]
[6,3,3,4]

[1,6,3,4,3,5]
[1,5,4,4,4,5]
[1,4,4,4,4,5]
1,2,3,4
len=6
1, 5


FAILED ON [2,1,2,1,1,2,2,1]
[2,1,2,1,1,2,2,1]
[2,2,2,1,1,2,2,1]

hmmm... i'm fundamentally misunderstanding something

what if you don't change it until everything is decided...?

ya that actually seems to be the answer
"""

class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            changes = {}
            for i in range(1, len(arr) - 1):
                if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    changes[i] = -1
                elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    changes[i] = 1
            if not changes:
                return arr
            for index, change in changes.items():
                arr[index] += change

"""
===== Initial Thoughts =====
target = 12, 
position = [10,8,0, 5,3], 
speed =    [2, 4,1, 1,3]
           [1, 1,12,7,3]


target = 10, position = [3], speed = [3]

target = 100, position = [0,2,4], 
                 speed = [4,2,1]

=== Brute Force Approach ===
compare all points with each other and determine where they will meet
if it's less than target, they group together. UF to keep groups. 
Return the number of groups

10 + 2x = 8 + 4x
2 = 2x
x = 1 

10 + 2x = x
x = -10 (negative means they will never match)

~~Complexity Analysis
Time - O(n^2)
Space - O(n)

=== Implemented Approach ===
Let's leverage their current positions

target = 12, 
position = [10,8,0, 5,3], 
speed =    [2, 4,1, 1,3]
[(0,1),(3,3),(5,1)]

position + speed * x = target

~~Complexity Analysis
Time - O(nlogn)
Space - O(n)
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = sorted([(p, s) for p, s in zip(position, speed)])
        p, s = stack.pop()
        timesteps = (target - p) / s
        num_groups = 1
        while stack:
            while stack and ((target - stack[-1][0]) / stack[-1][1]) <= timesteps:
                stack.pop()
            if stack:
                p, s = stack.pop()
                timesteps = (target - p) / s
                num_groups += 1
        return num_groups



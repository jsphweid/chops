"""
===== Initial Thoughts =====
gas = [2,3,4], cost = [3,4,3]
4-3+2 => 3-3+3

gas = [1,2,3,4,5], cost = [3,4,5,1,2]
[-2,-2,-2,3,3] => 0

[-2,-2,-2,3,3,-2,-2,-2,3,3]


[3,-3,-3,5]

gas = [2,3,4], cost = [3,4,3]
[-1,-1,1] => -1

=== Brute Force Approach ===
simulation

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 


failed on 
[1,2,3,4,5]
[3,4,5,1,2]
[-2,-2,-2,3,3,-2,-2,-2,3,3]

[5,8,2,8]
[6,5,6,6]
[-1,3,-4,2,-1,3,-4,2]

"""

def run(arr, i):
    l = len(arr) // 2
    curr = 0
    for i in range(i, i + l):
        num = arr[i]
        curr += num
        if curr < 0:
            return False
    return True


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        diff = diff + diff
        if sum(diff) < 0:
            return -1
        for i in range(len(gas)):
            if i > 0 and diff[i] <= diff[i - 1]:
                continue
            if i < 0:
                continue
            best = diff[i]
            if run(diff, i):
                return i

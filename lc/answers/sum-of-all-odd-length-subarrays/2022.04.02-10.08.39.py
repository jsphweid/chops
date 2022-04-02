"""
===== Initial Thoughts =====
[1,4,2,5,3] what if we summed them first...?
sum of 2:5 is 10

[0,1,5,7,12,15] means it's literally A[5] - A[2]

sum of 0:1 is A[1]-A[0]

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sums = [0]
        for num in arr:
            sums.append(sums[-1] + num)
        res = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) - i + 1):
                res += sums[j + i] - sums[j]
        return res

how could we do this with constant memory? use the original list...

~~Complexity Analysis
Time - O(n^2) (?)
Space - O(n)
"""

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr.insert(0, 0)
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        res = 0
        for i in range(1, len(arr), 2):
            for j in range(len(arr) - i):
                res += arr[j + i] - arr[j]
        return res



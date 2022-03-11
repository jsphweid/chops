"""
=== Brute Force Approach ===
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                curr = 1
                j = i-1
                while j >= 0 and arr[j] < arr[j+1]:
                    curr += 1
                    j -= 1
                j = i+1
                while j < len(arr) and arr[j] < arr[j-1]:
                    curr += 1
                    j += 1
                res = max(res, curr)
        return res

~~Complexity Analysis
Time - O(n^2)
Space-

=== Implemented Approach ===
one pass, two pointers

~~Complexity Analysis
Time-O(n)
Space-O(1)

anchor=0 i=2
"""

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3: return 0
        left, res = None, 0
        if arr[0] < arr[1]:
            left = 0
        for i in range(1, len(arr)-1):
            new_left = arr[i+1] > arr[i] and arr[i] <= arr[i-1]
            new_right = arr[i-1] > arr[i] and arr[i+1] >= arr[i]
            going_up = arr[i-1] < arr[i] < arr[i+1]
            going_down = arr[i-1] > arr[i] > arr[i+1]
            is_peak = arr[i] > arr[i-1] and arr[i] > arr[i+1]

            if new_right and left != None:
                res = max(res, i-left+1)
            if new_left:
                left = i
            elif going_up or going_down or is_peak:
                pass
            else:
                left = None
        if arr[-2] > arr[-1] and left != None:
            res = max(res, len(arr)-left)
        return res


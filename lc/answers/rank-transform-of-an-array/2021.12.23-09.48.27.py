"""
~~Complexity Analysis
Time - O(nlogn)
Space - O(n)

[40,10,20,30]
[10, 20, 30, 40]
d = {10: 1, 20: 2, 30:3, 40:4}
[4,1,2,3]


"""

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: return []
        sorted_arr = sorted(arr)
        d = {sorted_arr[0]: 1}
        for i in range(1, len(sorted_arr)):
            prev, curr = sorted_arr[i - 1], sorted_arr[i]
            d[curr] = d[prev] if prev == curr else d[prev] + 1
        return [d[num] for num in arr]


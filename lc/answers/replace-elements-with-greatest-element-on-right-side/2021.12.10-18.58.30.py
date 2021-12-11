class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res, largest = [], -1
        for i in range(len(arr) - 1, -1, -1):
            res.append(largest)
            largest = max(largest, arr[i])
        return res[::-1]
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        N = len(arr)
        arr.sort()
        d = N // 20
        lst = arr[d:N-d]
        return sum(lst) / len(lst)
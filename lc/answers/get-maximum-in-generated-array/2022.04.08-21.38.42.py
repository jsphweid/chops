class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2: return n
        lst = [0, 1]
        for i in range(2, n + 1):
            j = i // 2
            lst.append(lst[j] + (lst[j + 1] if i & 1 else 0))
        return max(lst)

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        streak, curr = 1, 0
        for i in range(len(arr) - m):
            if arr[i] == arr[i + m]:
                curr += 1
                if curr == m:
                    streak += 1
                    curr = 0
                if streak == k:
                    return True
            else:
                streak, curr = 1, 0
        return False
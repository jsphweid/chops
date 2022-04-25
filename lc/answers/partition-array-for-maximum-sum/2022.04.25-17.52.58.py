class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            best = 0
            for j in range(k):
                if ((i - j - 1) < 0): break
                best = max(best, arr[i - j - 1])
                all_of_em = best * (j + 1)
                dp[i] = max(dp[i], all_of_em + dp[i - j - 1])
        return dp[N]

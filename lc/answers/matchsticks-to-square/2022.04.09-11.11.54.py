"""
dfs(0,0,0,0,0)
    dfs(1,0,0,0,1)
        dfs(2,0,0,0,2)
            dfs(4,0,0,0,3)
            dfs(2,2,0,0,3)
                dfs(2,2,0,0,4)
                dfs(2,2,0,0,4)
                dfs(2,2,0,0,4)
                dfs(2,2,0,0,4)
            dfs(2,0,2,0,3)
            dfs(2,0,0,2,3)
        dfs(1,1,0,0,2)
        dfs(1,0,1,0,2)
        dfs(1,0,0,1,2)
    dfs(0,1,0,0,1)
    dfs(0,0,1,0,1)
    dfs(0,0,0,1,1)

sorting turns out to help a lot
"""

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4: return False
        total = sum(matchsticks)
        if total % 4: return False
        side = total // 4
        res = False
        matchsticks.sort(reverse=True)

        @lru_cache(None)
        def dfs(a, b, c, d, i):
            nonlocal res
            if res: return
            if i == len(matchsticks):
                if a == b == c == d == side:
                    res = True
            else:
                if res or max(a, b, c, d) > side:
                    return
                n = matchsticks[i]
                dfs(a + n, b, c, d, i + 1)
                dfs(a, b + n, c, d, i + 1)
                dfs(a, b, c + n, d, i + 1)
                dfs(a, b, c, d + n, i + 1)

        dfs(0, 0, 0, 0, 0)

        return res
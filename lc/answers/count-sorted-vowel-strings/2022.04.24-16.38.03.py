"""
===== Initial Thoughts =====
definitely dp in that you can build up answers bottom up
but they are only asking for count

=== Brute Force Approach ===
just build all the answers and then count them

class Solution:
    def countVowelStrings(self, n: int) -> int:
        letters = {
            "a": ["a", "e", "i", "o", "u"],
            "e": ["e", "i", "o", "u"],
            "i": ["i", "o", "u"],
            "o": ["o", "u"],
            "u": ["u"],
        }
        res = letters["a"]
        for i in range(1, n):
            temp = []
            for s in res:
                for letter in letters[s[-1]]:
                    temp.append(letter)
            res = temp
        return len(res)

=== Implemented Approach ===
did a bunch of work on the board and determined the DP approach

~~Complexity Analysis
Time - O(n) (since aeiou is always 5)
Space - O(n)
"""

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = []
        for i in range(5):
            dp.append([0] * n)

        for i, row in enumerate(dp):
            for j, _ in enumerate(row):
                dp[i][j] = 1 if (i == 0 or j == 0) else dp[i-1][j] + dp[i][j-1]

        res = 0
        for i in range(5):
            res += dp[i][-1]
        return res

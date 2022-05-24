"""
["10","0001","111001","1","0"]
[(1,1),(3,1),(2,4),(0,1),(1,0)]

["10","0001","111001","1","0"]
4
3

["10","0001","111001","1","0"]
5
3
dfs(0,5,3) -> 4
    0 - dfs(1,4,2) -> 3
        1 - dfs(2,1,1) -> 2
            3 - dfs(4,1,0) -> 1
                4 - dfs(5,0,0) -> 0
    1 - dfs(2,2,2)
    2 - None
    3 - dfs(4,5,2)
    4 - dfs(5,4,3)

Finally arrived at a brute force... :(

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        tallies = [(s.count("0"), s.count("1")) for s in strs]
        @cache
        def dfs(i, mm, nn):
            if i == len(tallies) or mm < 0 or nn < 0:
                return 0
            longest = 0
            for i in range(i, len(tallies)):
                zeros, ones = tallies[i]
                mmm = mm - zeros
                nnn = nn - ones
                if mmm >= 0 and nnn >= 0:
                    res = dfs(i + 1, mmm, nnn)
                    longest = max(longest, 1 + res)
            return longest
        return dfs(0, m, n)


I think a better solution takes advantage of smaller units being better than bigger units.
So if you sorted by 0's. Then another sorted by 1's. You could maybe run a greedy algo on that.

strs = ["10","0001","111001","1","0"], m = 5, n = 3
[0,1,10,0001,111001]

Came up with this greedy solution but failed..
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeros_ordered = sorted([(s.count("0"), s.count("1")) for s in strs])
        ones_ordered = sorted([(s.count("1"), s.count("0")) for s in strs])
        
        def find_longest(lst, l, r):
            longest = 0
            for ll, rr in lst:
                l -= ll
                r -= rr
                if l < 0 or r < 0:
                    break
                longest += 1
            return longest
        
        return max(find_longest(zeros_ordered, m, n), find_longest(ones_ordered, n, m))
        
["1100","100000","011111"]
6
6

which I suspected might happen

Reading answers... oh it's a knapsack problem... I don't know what that is though

reading this:
https://leetcode.com/problems/ones-and-zeroes/discuss/814077/Dedicated-to-Beginners

It's interesting how he views the problem slightly differently than me.
In my brute force, I view it as I choose one, then recurse with next options to choose
In his brute force, he views it as 'you can either use it or not use it and go to next'

["10","0001","111001","1","0"]
4
3

dfs(0,4,3)
    dfs(1,3,2) -> 4
        dfs(2,0,1) -> 3
            dfs(3,bad) -> 0
            dfs(3,0,1) -> 2
                dfs(4,0,0) -> 1
                    dfs(5) -> 0
                    dfs(5) -> 0
                dfs(4,0,1) -> 1
                    dfs(5,-1,1) -> 0
                    dfs(5,0,1) -> 0
        dfs(2,3,2)
    dfs(1,4,3)
    
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        tallies = [(s.count("0"), s.count("1")) for s in strs]
        
        @cache
        def solve(i, mm, nn):
            if mm < 0  or nn < 0:
                return -float("inf")
            if i == len(tallies):
                return 0

            # count it
            m_count, n_count = tallies[i]
            counted = 1 + solve(i + 1, mm - m_count, nn - n_count)

            # don't count it
            uncounted = solve(i + 1, mm, nn)
            return max(counted, uncounted)

        return solve(0, m, n)



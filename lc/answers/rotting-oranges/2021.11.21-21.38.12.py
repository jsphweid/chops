"""
===== Initial Thoughts =====
3
[2,2,2]
[2,2,0]
[0,2,2]

4
[2,2,2]
[0,2,2]
[1,0,2]

[[0,2]]

=== Brute Force Approach ===
scan the matrix, look for 2's and 1's, putting them in
different bins.

with the rottens, make a set of all neighbors that could be infected in a set
then iterate over all the non-rotten ones and see if any should be rotten now
put all new rotten oranges in a new bin... at the end of this iteration
assign new bin to the old bin of rotten ones and increment some
count by 1

if the number of fresh ones stays the same between two rounds,
then the game is over. return -1 if there are still fresh ones.
return the count (+1 ??? ) if not

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 


[2,1,1]
[1,1,0]
[0,1,1]
M=3 N=3 
bad={(0,0)} 
good={(0,1),(0,2),(1,0),(1,1),(2,1),(2,2)}
count=1
---- begin!
count=2 infect={(-1,0),(1,0),(0,-1),(0,1)} newly={(0,1),(1,0)}
bad={(0,1),(1,0)} good={(0,2),(1,1),(2,1),(2,2)}

count=3 infect={(1,1),(2,1),(-1,1),(0,0),(0,2),(1,-1)} newly={(0,2),(1,1),(2,1)}
bad={(0,2),(1,1),(2,1)} good={(2,2)} NOTE: I traced this slightly incorrectly

count=4 asdljfija dsljf al;f 

[[0,2]]
bad={(0,1)} good={}

[[2,1,1],[0,1,1],[1,0,1]]
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        bad, good = set(), set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1: good.add((i, j))
                if grid[i][j] == 2: bad.add((i, j))
        count = 0
        while len(good):
            count += 1
            infect, newly_infected = set(), set()
            for i, j in bad:
                infect.add((i - 1, j))
                infect.add((i + 1, j))
                infect.add((i, j - 1))
                infect.add((i, j + 1))
            for item in good:
                if item in infect: newly_infected.add(item)
            if not newly_infected: return -1
            bad = newly_infected
            good -= newly_infected
        return count

        
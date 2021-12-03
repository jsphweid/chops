"""
=== Brute Force Approach ===
just iterate over the rows doing the shift with a push/pop that many times

pop is O(1) but insert(0) is O(n)...
~~Complexity Analysis
Time - O(m*n*k)
Space - O(1 or m*n)

Actually ! I totally misunderstood the problem. We're not shifting per row, but instead 
over the whole thing.

We can still do simulation but calculation going to be much better...
Actually.. how about transposing it first, then transposing it back at the end...

basically the same time/space as above though, just using a proxy list

=== Implemented Approach ===
But what if we didn't have to do that inner step k times...?
(somehow the above brute force beats 94% tho..)

we'd need to maintain an extra copy of the list for ease
[1,2,3,4] -> [2,3,4,1] k=3
to shift 3... it's easy to imagine 0th index to 3... but how does 1 go to 0, then 2->1, 3->2
really... we just need to mod it.
0+3 % 4 => 3
1+3 % 4 => 0
2+3 % 4 => 1
etc.

let's try to solve for current_position
we need to inverse mod... HMMMMM
(current_position + k) % N = new_position
current_position%N + k%N = new_position
current_position%N = new_position - (k % N)

I'm missing something...

What if we try not to get too mathy. Why do we have to go in order?
Why don't we create a list already filled out with 0s and then jump around.
lst = [0] * N

Ok that works, but it ain't really so much faster for these smaller inputs.

How can we optimize further?



~~Complexity Analysis
Time - O(m*n)
Space - O(m*n)
"""

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        N = m * n
        lst = []
        for row in grid:
            lst += row
        lst2 = [0] * N
        for i in range(N):
            lst2[(i + k) % N] = lst[i]
        res = []
        for i in range(m):
            start = i * n
            res.append(lst2[start: start + n])
        return res
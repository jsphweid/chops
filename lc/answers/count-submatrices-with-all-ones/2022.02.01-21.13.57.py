"""
===== Initial Thoughts =====
1 0 1
1 1 0
1 1 0

let's start smaller

1 1
1 1 should have 9

even smaller

1 should have 1

1 1 should have 3
grows like 2 1

1 1 1 should have 6
grows like 3 2 1

1 1 1 1 should have 10
grows like 4 3 2 1

but how do we start stacking vertically
1
1 should be 3

1
1
1 should be 6. basically it behaves the same way

but how do combine it?

1 1
1 1 should be 9

4 2 this seems like it could make sense
2 1 the problem is that 4. It really should be a 5... But then that'd make 10, which is not true

6+12?
6 3
4 2
2 1

maybe it's add down, add right, add current, subtract diag?

3 0 1
4 2 0
2 1 0
works there

0 6 3 0
0 5 3 1
3 2 1 0
6+9+9
it just seems to work although I'm not quite sure why

~~Complexity Analysis
Time - O(n)
Space - O(1)

FAILED on [[1,0,1],[0,1,0],[1,0,1]]
1 0 1
0 1 0
1 0 1

My logic would subtract the middle because downright is 1.
If a num is 1, it has to be at least 1. So how do we handle this?
Do we make it minimum 1 or don't subtract if both sides are 0s.

What would happen in a similar case

1 0 1
0 1 0
1 1 1 should be 10

1 0 1
0 2 0
3 2 1 seems to make sense should only subtract if at least one of sides is not 0.

now failing on [[0,0,0],[0,0,0],[0,1,1],[1,1,0],[0,1,1]]
0 1 1
1 1 0
0 1 1

0 4 1
2 2 0
0 2 1

2 0 
2 1 should be 5, we have to subtract corner

1 2 0
0 2 1 should be 7. maybe we can only subtract a maximum of 1??

[[1,0,1],[1,1,0],[1,1,0]]
4 0 1
4 2 0
2 1 0


I just can't figure this out. Looking up the answer.

So apparently this is all off-base and this problem is a lot harder than this...

1 0 1 = 2
1 1 0 = 3
1 1 0 = 3
= = =
6 3 1

counting separately doesn't seem to work a

Found some brute force that I like and understand...

"""

def helper(mat, a, b):
    M, N, res = len(mat), len(mat[0]), 0
    for i in range(a, M):
        for j in range(b, N):
            if mat[i][j]:
                res += 1
            else:
                N = j
                break
    return res

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N, res = len(mat), len(mat[0]), 0
        for i in range(M):
            for j in range(N):
                res += helper(mat, i, j)
        return res







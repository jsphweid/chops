"""

total=4
[2,3,1,1,4,3,1,2,6,4,2]
 0 1 2                           c=1
   0 1 2 3                       c=2
         0 1 2 3 4               c=3
                 0 1 2 3 4 5 6   c=4

count=0 i=0 last=10
0<10
    count=1 n=2, 2+0 >= 10.. not true.. don't quit!
    range(1,3), j=1,2 [(4,1),(3,2)], set i=1
1<10 i=1
    count=2 n=3 4 >= 10 ? not, don't quit!
    range(1,4) j=1,2,3 [(2,2),(3,3),(7,4)], set i=4
4<10 i=4
    count=3 n=4 8>=last ?no, don't quit!
    range(1,5) j=1,2,3,4 [(4,5),(3,6),(5,7),(10,8)], set i=8
8<10 i=8
    count=4 n=6 14>=10.. yes it is... quit!

[1]
count=0, i=0 last=0

"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        count, i = 0, 0
        last = len(nums) - 1
        while i < last:
            count += 1
            n = nums[i]
            if i + n >= last: break
            _, i = max((j + nums[j + i], j + i) for j in range(1, n + 1))
        return count

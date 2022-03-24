"""
 0  1  2  3  4  5  6  7
[73,74,75,71,69,72,76,73]
stack=[7,6,2,1,0]
res=[0,0,1,1,2,4,1]

After this correct basically the same way as last time, I was wondering why a stack works.
[73,74,75,71,69,72,76,73]
In particular, when iterating backwards, we have index of 72, then 69 on the stack.
We evaluate 71 and know that the top of the stack (val 69) can't count as a valid answer
so we pop it. But WHY can we discard this information freely? How do we KNOW it won't be
needed later?

The reason is: if it can't be used as the answer to 71, then it has no other utility
as the problem specifies the next day at a higher temp. So at 75, we would check 71
but not 69. 69 has no value. Because if it were any value it would be 71 (which in 
this case doesn't even work). The stack works because it discards irrelevant smaller
numbers that won't be useful anymore.

If I do this again, I'll try to go from the front. And then maybe try some apparent
constant space solution.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            res.append(stack[-1] - i if stack else 0)
            stack.append(i)
        res.reverse()
        return res

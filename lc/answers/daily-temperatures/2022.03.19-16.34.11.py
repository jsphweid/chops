"""
=== Brute Force Approach ===
for each position, look at the sublist ahead of it and find the first number (if any)
that is larger... subtract the diff

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===
this is obviously a DP problem, which means its answer is mystereous

I can think of a sorting solution but it doesn't seem much better than brute force.
The idea is start from the right and insort items into a list. When looking for the
next result, you can get to the general area of results in logn time BUT the issue
is you still have to look through a group to find the most optimal.

temperatures = [73,74,75,71,69,72,76,73]

I looked in the back and found this idea of using a stack. I just read the title.
Then I read more in one of my books and feel more comfortable with the idea.

76

~~Complexity Analysis
Time - 
Space - 
 0  1  2  3  4  5  6  7
[73,74,75,71,69,72,76,73]

[76, 72, 69]

[89,62,70,58,47,47,46,76,100,70]
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            if not stack:
                res.append(0)
            else:
                while stack:
                    if temp >= stack[-1][0]:
                        stack.pop()
                    else:
                        res.append(stack[-1][1] - i)
                        break
                if not stack:
                    res.append(0)
            stack.append((temp, i))

        res.reverse()
        return res







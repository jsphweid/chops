"""
Never heard of Pascal's Triangle...

First way of solving could be simply use the previous layer and in-range indices to find the value
for the current row.

Another way would be to understand the pattern and just create it on a loop

Another thought is that we skip the whole triangle view because that's confusing... Just portray them as
lists... is anything obvious?
[
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, a, a, 5, 1]
]

I think the first idea I had is the most reasonable for a first pass.
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = [1]
            for j in range(1, i + 1):
                if j == i:
                    row.append(1)
                else:
                    row.append(result[i - 1][j] + result[i - 1][j - 1])

            result.append(row)
        return result


        
"""
=== Brute Force Approach ===
generate one row at a time and append it to a list

~~Complexity Analysis
Time - 0((n^2 + n)/2) or maybe just n^2 simplified
Space - same as Time really
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            row_length = i + 1
            previous = rows[i - 1]
            row = []
            for j in range(row_length):
                if j == 0 or j == row_length - 1:
                    row.append(1)
                else:
                    row.append(previous[j] + previous[j - 1])
            rows.append(row)
        return rows
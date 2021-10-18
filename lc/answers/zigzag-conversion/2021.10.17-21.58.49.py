"""
===== Initial Thoughts =====
P Y A I H R N
A P L S I I G

PAYPALISHIRING
PYAIHRNAPLSIIG

0,1,2,3,4,5,6,7,8,9,10,11,12,13
0,2,4,6,8,10,12,1,3,5,7,9,11,13

HOMER
H M R
O E
HMR
OE
024
13

How about with 3 rows?
HOMER
HR
OE
M

04
13
2



=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""
import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cycle = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        binning = cycle * math.ceil(len(s) / (len(cycle)))
        bins = [[] for _ in range(numRows)]
        for i, char in enumerate(s):
            bin_index = binning[i]
            bins[bin_index].append(char)
        return "".join(["".join(b) for b in bins])



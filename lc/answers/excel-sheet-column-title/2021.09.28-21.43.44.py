"""
===== Initial Thoughts =====
I remember this one... or was it the other related one...?
Shit... it's this one...
I remember a large part of this is avoiding 0's in middle. That's the tricky part.
Otherwise it is fairly straight-forward base-ish conversion (base-26)

=== Implemented Approach ===
7 is the max number of chars needed to represent 2 ** 31 - 1 (well 6.595, but we can't have just 0.595)
so that's 6-5-4-3-2-1-0 (26**n)


~~Complexity Analysis
Time - 
Space - 
"""

def get_minimums():
    # list containing the minimum remainder as to avoid 0's in the middle
    # A => 1, AA => 27, AAA => 703, etc.
    running_sum = 0
    minimums = [0]
    for i in range(6):
        new = 26 ** i
        minimums.append(new + running_sum)
        running_sum += new
    return minimums


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mins = get_minimums()
        letters = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        output = ""
        i = 6
        while i >= 0:
            fits = columnNumber // (26 ** i)
            if fits:
                remainder = columnNumber - (fits * (26 ** i))
                if remainder >= mins[i]:
                    output += letters[fits]
                    columnNumber = remainder
                elif fits > 1:
                    output += letters[fits - 1]
                    columnNumber -= ((fits - 1) * (26 ** i))
            i -= 1
        return output
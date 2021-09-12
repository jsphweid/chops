"""
This should be very easy...

For the first rule, we can just count the number of A's and make sure it's less than 2
For the 3 consecutive lates, we can just make sure LLL isn't in the list...
"""
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count("A") < 2 and "LLL" not in s
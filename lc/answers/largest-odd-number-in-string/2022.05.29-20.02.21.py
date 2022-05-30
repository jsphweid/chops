"""
===== Initial Thoughts =====
354272
371289
239480
35
923
9458
"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) & 1:
                return num[:i+1]
        return ""
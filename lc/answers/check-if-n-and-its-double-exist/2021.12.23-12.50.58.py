"""
[10,2,5,3]
10,2,5

[5,2,10,3]

[7,1,14,11]
7,1,
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num * 2 in seen or (num // 2 in seen and num % 2 == 0):
                return True
            seen.add(num)
        return False
        
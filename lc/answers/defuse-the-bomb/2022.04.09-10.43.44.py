"""
===== Initial Thoughts =====
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]

[5,12,13,17,22,29,30,34]
12,10,21,16

[2,4,9,3]
[2,6,15,18,20,24,33,36]
[12,13,6,5]
[5,6,13,12]

FAILED on 
[10,5,7,7,3,2,10,3,6,9,1,6]
-4

[10,15,22,29,32,34,44,47,53,62,63,69,79,84,91,98,101,103,113,116,122,131,132,138]
"""

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        L = len(code)
        if k == 0:
            return [0] * len(code)
        code = code * 2
        for i in range(1, len(code)):
            code[i] += code[i - 1]
        res = []
        if k > 0:
            for i in range(L):
                res.append(code[i + k] - code[i])
        else:
            k = abs(k)
            start = L - k - 1
            for i in range(start, start + L):
                res.append(code[i + k] - code[i])
        return res
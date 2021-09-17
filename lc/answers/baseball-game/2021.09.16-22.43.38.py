"""
seems pretty straight forward, but you never know with these problems...

["5","2","C","D","+"]
[5, 10, 15]
30

["5","-2","4","C","D","9","+","+"]
[5, -2, -4, 9, 5, 14]
27
"""

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for op in ops:
            if op == "C":
                record.pop()
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "+":
                record.append(sum(record[-2:]))
            else:  # is num
                record.append(int(op))  
        return sum(record)
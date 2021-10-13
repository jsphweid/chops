class Solution:
    def calPoints(self, ops: List[str]) -> int:
        lst = []

        for op in ops:
            if op == "C":
                lst.pop()
            elif op == "D":
                lst.append(lst[-1] * 2)
            elif op == "+":
                lst.append(sum(lst[-2:]))
            else:
                lst.append(int(op))

        return sum(lst)
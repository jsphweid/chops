"""
["4","13","5","/","+"]
[6]
bottom=5
top=13
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-/*":
                bottom, top = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(top + bottom)
                elif token == "-":
                    stack.append(top - bottom)
                elif token == "*":
                    stack.append(top * bottom)
                else:
                    stack.append(int(top / bottom))
            else:
                stack.append(int(token))
        return stack[0]

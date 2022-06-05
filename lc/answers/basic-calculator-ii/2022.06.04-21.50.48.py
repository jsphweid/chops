"""
===== Initial Thoughts =====
go through once for multi/div then again for add/sub?
use a stack?
"""

def process(left, right, operand):
    if operand == "+":
        return left + right
    elif operand == "-":
        return left - right
    elif operand == "/":
        return int(left / right)
    elif operand == "*":
        return left * right

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        acc = ""
        items = []
        for char in s:
            if char.isdigit():
                acc += char
            else:
                items.append(int(acc))
                items.append(char)
                acc = ""
        items.append(int(acc))

        # handle multi/div
        stack = []
        for item in items:
            if stack and stack[-1] in {"*", "/"}:
                operand, left = stack.pop(), stack.pop()
                stack.append(process(left, item, operand))
            else:
                stack.append(item)

        # handle add/sub
        final_stack = []
        for item in stack:
            if final_stack and final_stack[-1] in {"+", "-"}:
                operand, left = final_stack.pop(), final_stack.pop()
                final_stack.append(process(left, item, operand))
            else:
                final_stack.append(item)
        return final_stack[0]

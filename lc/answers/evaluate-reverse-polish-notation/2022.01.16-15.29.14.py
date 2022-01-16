"""
===== Initial Thoughts =====
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
probably use a stack
22

["2","1","+","3","*"]
9

["4","13","5","/","+"]
6

~~Complexity Analysis
Time - O(n)
Space - O(n)

tracing
["2","1","+","3","*"]
[9]

["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
[10,6,-132]

What I learned from this problem is that -2 // 10 is not 0... but instead -1.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token[-1].isdigit():
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                if token == "*":
                    stack.append(left * right)
                elif token == "/":
                    neg = (left < 0 and right >= 0) or (left >= 0 and right < 0)
                    res = abs(left) // abs(right)
                    stack.append(-res if neg else res)
                elif token == "+":
                    stack.append(left + right)
                else:
                    stack.append(left - right)
        return stack.pop()







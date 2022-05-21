"""
===== Initial Thoughts =====
T?T?F:5:3
T ? (T?F:5) : 3
look 5 pieces at a time
T?T?F, nope, so we say it's first 2 + next 5
T?F:3
["T?"]
5

expression="T?1:2:F?3:4"
stack=["F?"]

failed on
"T?5?7:7:T?6:T?2:F?T:T?2:T?T?F?F?F?4:T?F?5:T?F:T?F?4:9:9:6:3:9:5:T?F?F?F?F?5:2:9:6:F?4:T?6:7:T?8:F?0:F?F?5:T?F:5:T?T?9:4:F?F?T?F?F?6:8:F:4:F?F?T?F:F?F?0:F?7:2:T?8:T?F?9:8:7:1:6:T?T?F?9:T?F?3:8:3:F:4"

"T?T?5:F?7:7:T?6:T?2:F?T:T?2:T?T?F?F?F?4:T?F?5:T?F:T?F?4:9:9:6:3:9:5:T?F?F?F?F?5:2:9:6:F?4:T?6:7:T?8:F?0:F?F?5:T?F:5:T?T?9:4:F?F?T?F?F?6:8:F:4:F?F?T?F:F?F?0:F?7:2:T?8:T?F?9:8:7:1:6:T?T?F?9:T?F?3:8:3:F:4"


class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        while len(expression) > 1:
            if expression[1] == "?" and expression[3] == ":":
                if expression[0] == "T":
                    if stack:
                        rest = expression[5:]
                        expression = stack.pop() + expression[2] + rest
                    else:
                        return expression[2]
                else:
                    result = expression[4]
                    rest = expression[5:]
                    expression = stack.pop() if stack else ""
                    expression += result + rest
            else:
                stack.append(expression[:2])
                expression = expression[2:]
        return expression


Going for a different approach now. I'm not completely sure why it fails, but 
"""
class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        while len(expression) > 1:
            if expression[1] == "?" and expression[3] == ":":
                if expression[0] == "T":
                    if stack:
                        rest = expression[5:]
                        expression = stack.pop() + expression[2] + rest
                    else:
                        return expression[2]
                else:
                    result = expression[4]
                    rest = expression[5:]
                    expression = stack.pop() if stack else ""
                    expression += result + rest
            else:
                if expression[1] == "?" and expression[0] == "T" and not stack and expression[2].isdigit():
                    return expression[2]
                stack.append(expression[:2])
                expression = expression[2:]
        return expression

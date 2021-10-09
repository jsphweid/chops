import re
class Solution:
    def interpret(self, command: str) -> str:
        result = re.sub(r"\(\)", "o", command)
        result = re.sub(r"\(al\)", "al", result)
        return result
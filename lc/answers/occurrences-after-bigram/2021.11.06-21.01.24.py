import re
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        needle = first + " " + second
        return re.findall(rf"(?<=\b{needle}) ([a-z]+)", text)
import re
class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_spaces = len(re.findall(r"\s", text))
        words = re.findall(r"\w+", text)
        if len(words) == 1: return words[0] + (" " * num_spaces)
        between = num_spaces // (len(words) - 1)
        remainder = num_spaces % (len(words) - 1)
        joiner = " " * between
        return joiner.join(words) + (" " * remainder)
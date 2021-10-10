import re
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr: return True
        adjusted = ""
        for (letters, num) in re.findall(r"([a-z]+)|(\d+)", abbr):
            if letters: adjusted += letters
            if num:
                if num[0] == "0": return False
                if int(num) > len(word): return False
                adjusted += "1" * int(num)

        if len(word) != len(adjusted): return False

        for i in range(len(word)):
            left = word[i]
            right = adjusted[i]
            if left != right and right != "1":
                return False
        return True

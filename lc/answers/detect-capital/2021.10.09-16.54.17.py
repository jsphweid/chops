import re
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return bool(re.match("^[A-Z]?[a-z]*$|^[A-Z]*$", word))

import re
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        sep = "[a-z]*"
        regex = rf"^{sep + sep.join(list(pattern)) + sep}$"
        def matches(word):
            return bool(re.match(regex, word))
        return list(map(matches, queries))
import re
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        matcher = "[a-z]*"
        def matches(s: str) -> bool:
            return bool(re.match(rf"^{matcher}{matcher.join(list(pattern))}{matcher}$", s))
        return [matches(q) for q in queries]
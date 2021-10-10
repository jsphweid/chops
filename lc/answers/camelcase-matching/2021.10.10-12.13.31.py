"""
use regex to split the needle like FoBaT => Fo Ba T
each one needs to delete exactly 1 piece of string (if it can't delete, return False)
the remaining string must have no capital letters
"""

import re
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def is_match(word: str) -> bool:
            joiner = "[a-z]*"
            replaced = re.sub(f"({joiner.join(list(pattern))})", "", word)
            return len(re.findall(f"[A-Z]", replaced)) == 0
        
        return [is_match (q) for q in queries]
"""
===== Initial Thoughts =====
Build regex that matches certain character classes beginning to end
"""
import re
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [w for w in words if re.match("^[asdfghjkl]+$|^[qwertyuiop]+$|^[zxcvbnm]+$", w, re.IGNORECASE)]
        
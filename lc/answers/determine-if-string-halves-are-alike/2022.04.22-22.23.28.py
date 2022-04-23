class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        l = r = 0
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i in range(half):
            l += s[i] in vowels
            r += s[half + i] in vowels
        return l == r

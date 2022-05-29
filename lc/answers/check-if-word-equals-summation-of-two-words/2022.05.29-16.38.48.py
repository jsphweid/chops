class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def get_num(char):
            return str(ord(char) - ord("a"))
        def convert(word):
            return int("".join([get_num(char) for char in word]))
        return convert(firstWord) + convert(secondWord) == convert(targetWord)
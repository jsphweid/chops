class Solution:
    def reverseWords(self, s: str) -> str:
        words, buffer = [], ""
        for char in s:
            if char.isalnum():
                buffer += char
            else:
                if buffer:
                    words.append(buffer)
                    buffer = ""
        if buffer:
            words.append(buffer)
        return " ".join(reversed(words))
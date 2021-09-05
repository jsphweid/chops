"""
I failed this the first time because I assumed patterns always started with `a` but otherwise I think it works

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_pointer = 0
        chars = "abcdefghijklmnopqrstuvwxyz"
        acc = ""
        d = {}

        # iterate through words in s
        for word in s.split(" "):
            # if char pointer is greater than `z`, we want to return False already
            if char_pointer > 25:
                return False

            # if it's not in dict, then add to dict with the next available char as the value
            if word not in d:
                reserved_char = chars[char_pointer]
                char_pointer += 1
                d[word] = reserved_char

            # either way, add the char value to the accumulator
            acc += d[word]

        return acc == pattern


"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        used_letters = set()
        d = {}
        for i in range(len(words)):
            if words[i] in d:
                if d[words[i]] != pattern[i]:
                    return False
            else:
                if pattern[i] in used_letters:
                    return False
                d[words[i]] = pattern[i]
                used_letters.add(pattern[i])
        return True
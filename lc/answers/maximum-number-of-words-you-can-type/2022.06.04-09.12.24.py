"""
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bad = set(brokenLetters)
        bad_count = 0
        words = text.split(" ")
        for w in words:
            for char in w:
                if char in bad:
                    bad_count += 1
                    break
        return len(words) - bad_count


"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bad = set(brokenLetters)
        bad_count = 0
        curr_word_is_bad = False
        num_spaces = 0
        for char in text:
            if char in bad:
                curr_word_is_bad = True
            if char == " ":
                bad_count += curr_word_is_bad
                curr_word_is_bad = False
                num_spaces += 1
        bad_count += curr_word_is_bad
        num_words = num_spaces + 1
        return num_words - bad_count

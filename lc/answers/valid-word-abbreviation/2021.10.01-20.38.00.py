"""
===== Initial Thoughts =====
I think a two pass solution can work

=== Implemented Approach ===
go through once, separating out digits, when a char is encountered and digits buffer exists
then put in x's before adding the char
then do a comparison between lengths
then do a comparison letter by letter... each letter should match exactly or be x

~~Complexity Analysis
Time - O(n)
Space - O(n)
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        digit_buffer = ""
        alt_word_buffer = ""
        for char in abbr:
            if char.isdigit():
                if not digit_buffer and char == "0":
                    return False
                digit_buffer += char
            else:
                if digit_buffer:
                    expanded = int(digit_buffer)
                    if expanded > len(word): # handles the cases when number is REALLY large
                        return False
                    alt_word_buffer += "x" * expanded
                    digit_buffer = ""
                alt_word_buffer += char
        if digit_buffer:
            expanded = int(digit_buffer)
            if expanded > len(word): # handles the cases when number is REALLY large
                return False
            alt_word_buffer += "x" * expanded
        if len(word) != len(alt_word_buffer): return False
        for left, right in zip(word, alt_word_buffer):
            if left != right and right != "x":
                return False
        return True
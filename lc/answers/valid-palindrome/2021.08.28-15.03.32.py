"""
An easy way to solve this would be to have a regex that eliminates all unnecessary characters
and converts everything to lowercase. Then it asserts the reversed form is the same as the
unreversed form.

But I don't know regex.

Another way would be to use ord and assert ascii ranges. I think that is the most reasonable thing
to do for now.

*confirm alphanumeric is just numbers and letters, upper and lowercase? So a-zA-Z0-9?

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # iterate over each char
        # for each, determine if in proper ascii range, if it is add to str
        # lower case str
        # return a comparison with its reversed form

        A_LOWER = 97
        Z_LOWER = 122
        A_UPPER = 65
        Z_UPPER = 90
        ZERO = 48
        NINE = 57

        def _char_is_alphanumeric(char: str) -> bool:
            ascii_value = ord(char)
            return (A_LOWER <= ascii_value <= Z_LOWER) or (A_UPPER <= ascii_value <= Z_UPPER) or (ZERO <= ascii_value <= NINE)

        string = ""
        for char in s:
            if _char_is_alphanumeric(char):
                string += char
        string = string.lower()
        return string == "".join(list(reversed(string)))

        
"""
This may use a tiny bit more memory but is probably more efficient
than my last solution. It's also easier to read and I could've implemented
it without looking at ord values...
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        new_str = ""
        for char in s:
            if char in alphanumeric:
                new_str += char
        new_str = new_str.lower()
        return new_str == "".join(list(reversed(new_str)))

"""
failed once because I forgot to lower()
"""
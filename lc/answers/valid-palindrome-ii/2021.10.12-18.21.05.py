"""
=== Brute Force Approach ===
go through every char, deleting it, checking if remaining string is a palindrome by reversing etc.

~~Complexity Analysis
Time - O(n2) where n is length of s
Space - O(n) - space for making the new str

=== Implemented Approach ===
thinking about counts. a palindrome can be made if all the characters are even length. If one is odd, then you can't
make a palindrome.

hmm, when you encounter an error, you can either delete the left or right. We kind of need to check both sides.
So I'm going to make an inner palindrome checker. When I encounter an error, I'll pass it to the inner checker but with
some flag indicating it can't have any margin of error.

~~Complexity Analysis
Time - O(2n)
Space - O(2n)
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid(string: str, fail_on_error: bool) -> bool:
            left, right = 0, len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    if fail_on_error:
                        return False
                    else:
                        return is_valid(s[left: right], True) or is_valid(s[left + 1: right + 1], True)
                left += 1
                right -= 1
            return True

        return is_valid(s, False)
"""
brute force would involve getting all permutations and then checking each if it's a palindrome.
But I feel like there is a better way to solve this problem. For a palindrome to be possible
there are some basic conditions that have to be met. Like if the length is odd, one char
has to be occuring only once. The other chars have to occur an even amount of times. So
an algorithm that could be used here would involve nothing other but efficiently checking
these occurences.

We could iterate over the string getting the occurences of each as values.

lengths in ascending order would be something like [1, 2, 2, 4, 6, 8] for an odd palindrome
for even length palindrome, all lengths would need to be even.

Really we could have one variable max_odds_allowed = 1 if (len(s) & 1) else 0


"""

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # determine unique chars
        unique_chars = set(s)
        # get an array with counts off each char
        counts = [s.count(char) for char in unique_chars]
        # find out how many odds are allowed
        num_odds_allowed = len(s) & 1
        # ensure array of counts only has that many odds
        return num_odds_allowed == len([c for c in counts if c & 1])
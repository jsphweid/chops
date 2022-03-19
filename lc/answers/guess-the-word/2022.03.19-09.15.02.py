"""
===== Initial Thoughts =====
secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"], numguesses = 10
1. try a word, assuming it fails, eliminate all other words that DON'T have the same number in common
2. reorder the list so the words with most shared letters are at the front
like wordle... there is a most statisticly based word to lead with
unlike wordle, you get more limited information from each guess. So a simple ordering will suffice.

I messed up my sorting algorithm.
["acckzz","ccbazz","eiowzz","abcczz"]
6 3 2 4
3 6 2 2
2 2 6 2
4 2 2 6

previously I was prioritizing highest scores... so the first item would've had the biggest priority
but I don't think that's what we actually want... when we pick one, we want to eliminate the most
if it's wrong
"""

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def similarity_score(word1, word2):
            return sum([l == r for l, r in zip(word1, word2)])

        def get_score(word):
            return sum([similarity_score(word, other) for other in wordlist])

        wordlist = sorted(wordlist, key=get_score)

        for _ in range(10):
            if wordlist:
                word = wordlist.pop()
                master_score = master.guess(word)
                if master_score == 6:
                    return

                remaining = []
                for other in wordlist:
                    if similarity_score(word, other) == master_score:
                        remaining.append(other)
                wordlist = remaining











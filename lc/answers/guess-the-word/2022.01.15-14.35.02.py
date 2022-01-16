"""
===== Initial Thoughts =====
["acckzz","ccbazz","eiowzz","abcczz"]
acckzz 4
ccbazz 3
eiowzz 2
abcczz 4

    acckzz - 2 
    ccbazz - 3
w   eiowzz - 2
    abcczz - 4



=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

def get_sim(one, two):
    return sum([one[i] == two[i] for i in range(6)])

from collections import defaultdict

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        d = defaultdict(int)
        for word in wordlist:
            for other in wordlist:
                d[word] += get_sim(word, other)
        tuples = list(d.items())
        tuples.sort(key=lambda x: x[1])
        wordlist = [item[0] for item in tuples]

        while wordlist:
            word = wordlist.pop()
            res = master.guess(word)
            if res == 6:
                return
            wordlist = [w for w in wordlist if get_sim(word, w) == res]



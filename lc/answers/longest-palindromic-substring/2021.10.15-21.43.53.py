"""
===== Initial Thoughts =====
hmmm... i'm nervous

=== Brute Force Approach ===
get every possible substring. if it beats some previous longest length, set it
to the new winner.

babad
baba
bab - palindrome (valid answer)
ba
b - palindrome

abad
aba - palindrome (valid answer)
ab
a - palindrome

bad
ba
b - palindrome

ad
a - palindrome

d

I don't really see a way around this whole afair

~~Complexity Analysis
Time - O(n^2 * n)
Space - O(len(s))

=== Implemented Approach ===
I know DP should be used... but how?
checking the palindrome is expensive and possibly redundant
0,4 1,3
0,3 1,2

babad 0,4 1,3
baba 0,3 1,2
bab 0,2
ba 0,1
b

abad 1,4 2,3
aba 1,3 (DUPLICATE)
ab
a

on larger strings there will be a lot more...

babad, len=5, 
range(0, 4) => 0, 1, 2, 3, 4
range(1, 5) => 1, 2, 3, 4, 5

cbbd, len=4
range(0, 3) => 0, 1, 2, 3
range(1, 4) => 1, 2, 3, 4

UPDATE: read some answers and I think I'm ready to implement this with DP.

the trick here is understanding that something is a palindrome if the left+1 and right-1
are also palindromes IF you have checked those already. You MUST check them in the correct
order. The order has to be such that the whole string is checked LAST. So the typical
```
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
```
stuff won't work here. 

for example, in "aabaa" it will check 0,4 before it checks 1,3... that's bad!

The pattern that does work is to iterate the end on the outside and the
start on the inside, iterating backwards

0,1
1,2 0,2
2,3 1,3 0,3
3,4 2,4 1,4 0,4 (0,4 is whole string and checked last)

the other thing is we need to build from the ground up if we're not going to have a
palindrome fn.. So we need to start with 0,0 1,1 etc.

~~Complexity Analysis
Time - O(n^2)
Space - O(n^2)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {(i, i) for i in range(len(s))}
        winning_length = 1
        winner = (0, 0)
        for end in range(1, len(s)):
            for start in range(end - 1, -1, -1):
                if s[start] == s[end]:
                    if end - start == 1 or (start + 1, end - 1) in dp:
                        dp.add((start, end))
                        l = end - start + 1
                        if l > winning_length:
                            winner = (start, end)
                            winning_length = l
        return s[winner[0]: winner[1] + 1]

"""
I think this is similar to other palindrome questions in that that ratio of evens/odds matter.
We can classify a string as palindrome if:
length of string odd? all char counts are even except 1
length of string even? all char counts are even

to say that we can delete 1 char is essentially asking us if we delete "a certain char", does it put
us in those categories above.

The question is largely, does such an eligible char exist, such that it puts us in those above categories
when deleted.

But wait, there's more... it says "at most", which means that if it already satisfies the categories 
above then it is true.

We could
    1. see if it's already eligible
    2. see if deleting one makes it eligible
        - if currently even length: there's never any sense deleting anything
        - if currently odd, can we put it into all odds except one by deleting an odd
            - i.e. is it 3, 3, 4, 6, 6, 4, 6,  (i.e. two are odd, max)
            - really all we are saying "are there two odds and the rest are even"

*** final "max odds are 2 or less"

ACTUALLY THIS FAILS because I'm not considering order. Similar questions on here consider orderless
approaches to answering this question ("Is palindrome possible with these chars"). I misunderstood this.

```
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        return len([q for q in d.values() if q & 1]) < 3
```
That was my original solution.

How does this change things

we mandate [even even even even even even]
or [even even odd even even] or [even even odd odd even even] etc.
if we were to do counts... it'd look like [even even even odd] or [even even even odd odd]

it's essentially giving you one odd allowance
in `abca` it works because a == a and b != c... normally this is a deal breaker but since that makes
the count of "deal breakers" 1 and only 1, then it's okay. But it has to be at the end

```
    def validPalindrome(self, s: str) -> bool:
        bad_detected = False
        is_odd = len(s) & 1
        for i in range(len(s) // 2):
            if bad_detected:
                return False
            if s[i] != s[len(s) - 1 - i]:
                if is_odd:
                    return False
                else:
                    bad_detected = True
        return True
```
this was my second solution that did pretty well but not on strings like `deeee`. Clearly I didn't consider
that a string can be odd with a little forgiveness

I think I may have overcomplicated it a bit...

Maybe we can go with "if a bad pair is discovered, delete one" then compare strings at end
but we have to consider the original string being a palindrome as well

Failed again... can't change string with assignment

Failed again... (damn... too much bourbon possibly) you delete! not replace...

Failed again
`"cbbcc"`
cbbcc

This is a serious case of crash and burn

```
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        s_list = list(s)

        change_used = False
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                if change_used:
                    return False
                else:
                    s_list.pop(i)
                    change_used = True
        return s_list == s_list[::-1]
```

The issue is that it may be more beneficial to delete from the "other side"... i.e. instead off 
cbbcc -> cbcc (which is not a palindrome)... cbbcc -> cbbc (which is)

I have failed. Seeing "2 line C++ solution" title in the "Discuss" makes me feel worse. I dont' want 
to look at the answer. I know this is easy. Why am I making it so complicated?
cbbcc -> True {c: 3, b: 2}
abca -> True {a: 2, b: 1, c: 1}
aba -> True {a: 2, b: 1}
abc -> False {a: 1, b: 1, c: 1}
eedede -> True edede
[e e d e d e ]
[e d e d e ]
[e e d e e ]
"""
from collections import defaultdict

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        s_list = list(s)
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                left = list(s)
                right = list(s)
                left.pop(i)
                right.pop(len(s) - 1 - i)
                return (left == left[::-1]) or (right == right[::-1])
        return True

            
        
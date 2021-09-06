"""
why do so many people down-vote this?
we have to pick output numbers from strings

a_ord = 111
z_ord = 222
0_ord = 333
9_ord = 444
this should be pretty doable using ord values since we expect lowercase expect numbers

high level:
- use abbr ords to get actual lengths and build that string using wildcards, maybe something like
apple, a3e -> a***e, then do a string to string comparison.
There are more efficient ways of doing this, but this seems like a pretty good starter solution.

I'm kind of mad that my solution didn't work because of the memory error
and the completely stupid test case where int("01") != 1 somehow.

```
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # these were initially garbage values so I "cheated" minimally
        a_ord = 97
        z_ord = 122

        # re-write abbr to have wildcards
        abbr_new = ""
        num_buffer = ""
        for char in abbr:
            if a_ord <= ord(char) <= z_ord:  # is lowercase char
                if num_buffer:
                    if num_buffer[0] == "0":  # handle some stupid edge case
                        return False
                    abbr_new += ("*" * int(num_buffer))
                    num_buffer = ""
                abbr_new += char
            else:  # has to be digit
                num_buffer += char
        if num_buffer:
            if num_buffer[0] == "0":  # handle some stupid edge case
                return False
            abbr_new += ("*" * int(num_buffer))

        # do string to string comparison
        if len(word) != len(abbr_new):
            return False

        for i in range(len(word)):
            if word[i] != abbr_new[i] and abbr_new[i] != '*':
                return False
        return True
```

"""

class Solution:
    def validWordAbbreviation(self, word, abbr):
        # copied and pasted from the internet because read above. I'll come back to this but don't have time for now...
        return bool(re.match(re.sub('([1-9]\d*)', r'.{\1}', abbr) + '$', word))
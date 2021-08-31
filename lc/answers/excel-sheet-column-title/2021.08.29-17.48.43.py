"""
this is base-26, so it's a bit weird to think about but we can basically
iterate over the max num size doing division by 26**5, 26**4, etc.

We have to do a little bit of calculating to find a good starting number. Actually,
I think I'll just go with 8 because I see their max string is "FXSHRXW", 7 chars long.

So starting with 26 * 26**8, we step down and see if there is an int division that is greater
than 0. A non-zero value indicates how many of that char can go in there

===============

I was getting loopy last night. This morning I decided to start over.

A - 1
B - 2
AA - 3
AB - 4
BA - 5
BB - 6
AAA - 7
AAB - 8
ABA - 9
ABB - 10
BAA - 11
BAB - 12
BBA - 13
BBB - 14

12
2^2, 2^1, 2^0
2  , 1  , 2
8

13
2  , 2  , 1

14
2  , 2  , 2

2^3, 2^2, 2^1, 2^0
1  , 1  , 1  , 0

The fundamental problem is that there is no zero! With this approach it seems, we must produce
a remainder such that all the powers presence has at least 1 or 2.
1. if we discover a 0 after we've already started accumulating chars, then we have to start
with a smaller power.
2. if a power covers a number perfectly, we have to use a smaller power unless it's the last.
3. in the AB scheme, obviously we can only use 1 or 2 as numbers of numbers of powers

Talked to Aaron about it and there is an easy way to solve the remainder issue.

A - 1
B - 2
AA - 3
AB - 4
BA - 5
BB - 6
AAA - 7
AAB - 8
ABA - 9
ABB - 10
BAA - 11
BAB - 12
BBA - 13
BBB - 14

Basically, if we have a 3 digit num here with our base-2 example, We can't accept a number where the remainder is less than the number
what the number of powers left can provide. So with 16 for example we cannot solve the MSB such that the remaining is below 7. To solve
the second bit, we have to stay about 3... etc.
1, 3, 7, 15
2^1 - 1, 2^2 - 1, 2^3 - 1, 2^4 - 1
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # it's 1-indexed
        values = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = columnNumber
        output = ""
        power = 8
        while power >= 0:
            result = num // (26 ** power)
            if result:
                result = min(result, 26)
                amount_to_take_away = result * (26 ** power)
                minimum_value_to_leave = (26 ** power) // 25
                if num - amount_to_take_away < minimum_value_to_leave:
                    if result == 1:
                        power -= 1
                        continue
                    else:
                        result -= 1
                        amount_to_take_away = result * (26 ** power)
                output += values[result]
                num -= amount_to_take_away
            power -= 1
        return output





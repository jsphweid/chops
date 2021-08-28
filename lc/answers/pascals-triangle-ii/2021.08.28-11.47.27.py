"""
In the first one, we had to render the entire triangle but in this one, we just
need a single row which heavily encourages NOT making the entire triangle, since
that's a waste of time when we only need 1 row from it.

Let's visualize this again:
[
    0 - [1]
    1 - [1, 1] - 0
    2 - [1, 2, 1] - 1, 1
    3 - [1, 3, 3, 1] - 2, 0, 2
    4 - [1, 4, 6, 4, 1] - 3, 2, 2, 3
    5 - [1, 5, 10, 10, 5, 1] - 4, 5, 0, 5, 4
    6 - [1, 6, 15, 20, 15, 6, 1] - 5, 9, 5, 5, 9, 5
    7 - [1, 7, 21, 35, 35, 21, 7, 1] - 6, 14, 14, 0, 14, 14, 6
    8 - [1, 8, 28, 56, 70, 56, 28, 8, 1] - 7, 20, 28, 14, 14, 28, 20, 7
    9 - [1, 9, 36, 84, 126, 126, 84, 36, 9, 1] - 8, 27, 48, 42, 0, 42, 48, 27, 8
]

If we want to humor this approach, we kind of have to only think about
the pattern as it pertains to one row. Don't look at the other rows.

I made a difference list on the visualization above and while it's interesting,
I'm not sure I'm getting any closer to an answer.

[
    0 - [1]
    1 - [1, 1]
    2 - [1, 2, 1] second * 1 - 1, ???
    3 - [1, 3, 3, 1] second * 1, ???
    4 - [1, 4, 6, 4, 1] second * 2 - 2,
    5 - [1, 5, 10, 10, 5, 1] second * 2,
    6 - [1, 6, 15, 20, 15, 6, 1] second * 3 - 3, second * 4 - 4
    7 - [1, 7, 21, 35, 35, 21, 7, 1] second * 3, second * 5
    8 - [1, 8, 28, 56, 70, 56, 28, 8, 1] second * 4 - 4, second * 7
    9 - [1, 9, 36, 84, 126, 126, 84, 36, 9, 1] second * 4,  
]

This is hard because there are so many patterns going on that it's difficult
to understand which one will lead me in the right direction...

[
    0 - [1]
    1 - [1, 1]
    2 - [1, 2, 1]
    3 - [1, 3, 3, 1]
    4 - [1, 4, 6, 4, 1] 4-1 * 2
    5 - [1, 5, 10, 10, 5, 1] 5 * 2
    6 - [1, 6, 15, 20, 15, 6, 1] 6-1 * 3, 6-1 * 4
    7 - [1, 7, 21, 35, 35, 21, 7, 1] 7 * 3, 7 * 5
    8 - [1, 8, 28, 56, 70, 56, 28, 8, 1] 8-1 * 4, 8-1 * 5, nope
    9 - [1, 9, 36, 84, 126, 126, 84, 36, 9, 1] 9 * 4
]

This isn't working out... let's just think about complex row...
We need to possibly involve the index into the calculation...?
9 - [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
     0  1  2   3   4
  diff  8, 27, 48, 42
           35, 75, 90

Wait a minute...
0 - 1 -> 9 * 0 * 0 (+1), but doesn't matter
1 - 9 -> 9 * 1 * 1
2 - 36 -> 9 * 2 * 2
3 - 84 -> 9 * 3 * 3 (+3)
4 - 126 -> 9 * 4 * 4 (-18)

Not quite... but maybe there is something there...

Let's look at 8... I need to see different numbers...
8 - [1, 8, 28, 56, 70, 56, 28, 8, 1]
     0  1  2   3   4
What's weird is the jumps get smaller at some point...
28->56 big jump. 56->70, relatively small jump
I think I might need to look at the original problem statement. Since each number
depends on the ones above it it might be a little difficult to get around
the dependency problem. Not sure if we can take a shortcut...

Although now I'm curious about solving the original problem recursively...

Actually I can solve this recursively? We can think about that later.

This HAS to be possible...

8 - [1, 9, 36, 84, 126]
     0  1  2   3   4

What if it has more to do with 8, since that is a component from the row above?

Nah, let's look at bigger numbers...
    9  - [1, 9, 36, 84, 126]
    10 - [1, 10, 45, 120, 210, 252]
    11 - [1, 11, 55, 165, 330, 462, 504?]
Let's go back to that idea where all the numbers get bigger, but by less that previous,
like for 9
    a. 9 is 9 times the size of 1
    b. 36 is 4 times the size of 9
    c. 84 is 2.333 times the sie of 36
    d. 126 is 1.5 times the size of 84

for 10
    a. 10 is 10 times the size of 1
    b. 45 is 4.5 times the size of 10
    c. 120 is 2.6666 times the size of 45
    d. 210 is 1.75 times the size of 120
    252 is 1.2 times the size of 210

for 11
    a. 11 is 11 times the size of 1
    b. 55 is 5 times the size of 11
    c. 165 is 3 times the size of 55
    d. 330 is 2 times the size of 165
    462 is 1.4 times the size of 330
    not sure about last one immediately

pattern
a. 1st index - x times is increasing by 1 (1/1)
b. 2nd index - x times is increasing by 0.5 (1/2)
c. 3rd index - x times in increasing by 0.333 (1/3)
d. 4th index - x times is increasing by 0.25 (1/4)

so the it's increasing by a fraction of the index from the previous number or
something like that. It's still all clear but at this point it's pretty obvious 
I'm on the right path.

n is the row they asked for...
0th index is always 1
1st index is 0th * (n-i+1 * 1/i)
2nd index is 1st * (n-i+1 * 1/i)
3rd index is 2nd * (n-i+1 * 1/i)

DOWNSIDE: floating point operations... I wonder if there is a way to solve it that
doesn't use that division?
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        midpoint = rowIndex // 2
        for i in range(1, midpoint + 1):
            result.append(round(result[i - 1] * ((rowIndex - i + 1) / i)))

        # if rowIndex is odd, it has the repeated number
        return result + list(reversed(result[0:midpoint + (rowIndex % 2)]))

"""
Failed first time because I second-guessed myself on the rowIndex % 2... 
I was already thinking about it, but had it wrong so I took it out. But
after going over a few more examples, I re-implemented it correctly.

The other failures were because of rounding. Even if something divides evenly,
it'll get put in float land if you're not careful. But throwing a simple int()
in there is also not good because it'll round 1.99999 to 1 for example when
you really wanted 2. So `round` is appropriate. Overall my approach was solid,
although it took a long time to arrive

I think this code
        if rowIndex == 1:
            return [1, 1]
can be removed...? Yes.

Can this one be removed
        if rowIndex == 0:
            return [1]
can be removed...? Also yes.
"""


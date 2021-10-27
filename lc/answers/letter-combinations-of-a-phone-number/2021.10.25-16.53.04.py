"""
===== Initial Thoughts =====
Aaron and I talked quite a bit about these various solutions. My idea was more along the lines
of counting in indices. For example. Say we want to combine two lists that each have length 2.
The combinations look like this in terms of indices...
00
01
10
11
Look familiar? We are counting... in binary

The problem is that the lists will have lengths other than 3. For example, 7/9 have 4.
So really we need to count in multiple bases.

That sounds kind of fun to implement!

It shouldn"t be too entirely different from regular counting algorithms.
If we"re counting in base 3, a normal algorithm might look like
def fn(num: int) -> List[int]:
    # assume it can be represented with 4 digits...
    output = []
    for i in range(3, -1, -1):
        n = 3 ** i
        output.append(num // n)
        num -= ((num // n) * n)
    return output

We can adjust that with multiple bases... instead of 3 ** i,... we can just use j ** i, when j
in the length of the list

Ok, so my result failed... this fn doesn't work
        def fn(num: int, bases: List[int]) -> List[int]:
            output = []
            for i in range(len(bases)):
                power = len(bases) - 1 - i  # just the inverse count
                n = bases[i] ** power
                output.append(num // n)
                num -= ((num // n) * n)
            return output

It makes sense why it failed after a bit of tracing. Normally you can count the powers
like 10**3, 10**2, 10**1, 10**0, etc. I was initially thinking instead of 10s, you could use the
length of each item in the list, but this doesn't work.

for example, say we have [['a', 'b']['c', 'd', 'e']['f', 'g']]
that's 2 3 2... instead of 10 10 10, we have 2 3 2
that's essentially saying how many 2**2's are there, 3**1's are there, and 2**0's are there
so 4's 3's 1's
This can't adequately represent a number. For example, how could it represent two? There are no
4's in two. There are no 3's in two. There are 2 1's in two, but we can't use it because that last
list only has 2 elements and arr[2] is out of range. It just doesn't work.

I was looking at this incorrectly. What we should be looking at is the number in a group. For example:
000
001
010
011
020
021
100
101
110
111
120
121

the left group has groups of 6. the middle group has groups of 2. the right group has groups of 1.
We get these groups by multiplying 2*3*2, then divde by 2, then 3, then 2.

Aaron immediately arrived at this last night but for some reason
my dumb brain had to go all the way down the wrong path first.

I'm trying desperately to thinking how this represents itself in ordinary counting.
000
001
010
011
100
101
110
111

first group is divided by 2. Then 2. Then 2. i.e. 4->2->1. It works with ordinary counting too.

I guess my brain was more along the thought of the base**power, but maybe counting has more
to do with how many groups of each digit there are. It's the same result with these fixed size
bases. But it becomes more obvious when the bases are variable sized.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def get_group_sizes(bases: List[int]) -> List[int]:
            total = 1
            for l in lengths: total *= l
            res = []
            for base in bases:
                c = total // base
                res.append(c)
                total = c
            return res

        def fn(num: int, group_sizes: List[int]) -> List[int]:
            output = []
            for i in range(len(group_sizes)):
                n = group_sizes[i]
                output.append(num // n)
                num -= ((num // n) * n)
            return output

        combinations = [mapping[d] for d in digits]
        lengths = [len(c) for c in combinations]
        group_sizes = get_group_sizes(lengths)
        total = 1
        ans = []
        for l in lengths: total *= l
        for x in range(total):
            indices = fn(x, group_sizes)
            s = ""
            for i, index in enumerate(indices):
                s += combinations[i][index]
            ans.append(s)
        return ans

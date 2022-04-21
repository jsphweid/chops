"""
===== Initial Thoughts =====
odd but straight-forward I think

for "(()))", we build up 2 ('s immediately... meaning we need 4 )'s to
counteract... We only get 3. We need one more

))())(
))(

I think we can use a stack which is O(n) / O(n)
We just process it once then whatever is left we use that to count missing items.

"))())("
after processing... => "))("

)), we're missing a (
(, we're missing ))
so 3

That's a little difficult to code though.
What if we had )(? We know it's 4, it's just a little tricky to count

"(())())))"

we'll just have to go through it again

~~Complexity Analysis
Time - O(n)
Space - O(n)

"))())("
[")", ")", "("]
()


class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        for char in s:
            if char == ")" and len(stack) >= 2 and stack[-1] == ")" and stack[-2] == "(":
                stack.pop()
                stack.pop()
            else:
                stack.append(char)

        # count
        res = l = r = 0
        for char in stack:
            if char == ")": r += 1
            if char == "(": l += 1

            if r == 2:
                res += 1
                r = 0
            elif l == 1 and r == 1:
                res += 1
                l = r = 0
            elif l == 2:
                res += 2
                l = 1
        if l == 1 and r == 1:
            res += 1
        elif l == 1 or r == 1:
            res += 2

        return res

original solution doesn't work because I didn't fundamentally understand the problem. We can't
do the stack thing because of the chain reactions, which are apparently bad. I need to understand
that more...

replace our stack part with this: `stack = list(s.replace("())", ""))`

But then it fails on this... "((())))))" apparently chain reactions are ok on this. I'm confused.
" (..........(.........) .........) ....... )...........(...........(........ ).........).........) ........(......... )........(............ )......... ) ....... ).........)"
" 0.........1........2........3 .......4.........5..........6......7.........8.........9.......10.....11......12......13.......14......15......16"

((()))

))())(
[)

[)

))())(
][][
][

"()" => 1
"))())("
]( => 3

0
r=0
l=0

(((()(()((((()]()](((()(()()((())
((((

"](](" ->(3)


"""

class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        res = 0
        for char in s.replace("))", "]"):
            if char == "(":
                stack.append(char)
            elif char == ")":
                if stack:
                    stack.pop()
                    res += 1
                else:
                    res += 2
            elif char == "]":
                if stack:
                    stack.pop()
                else:
                    res += 1
        return res + len(stack) * 2

"""
((()))
(()())
()()()
(())()
())(()

(((()))) 4
((()())) 11 wrapped * 2
(()()()) 111 wrapped
()()()() 1111

(())()() 211
()()(()) 112
()((())) 1 3
((()))() 3 1

I made this but I'm very sure it's not close to working...
        seed1 = "()" * n
        seed2 = ("(" * n) + (")" * n)
        res = set([seed1, seed2])

        def process(seed):
            for i in range(2, len(seed) - 1):
                lst = list(seed)
                right = lst[i]
                lst[i - 1] = lst[i]
                lst[i] = right
                res.add("".join(lst))

        process(seed1)
        process(seed2)
        return list(res)

I could explore that above pattern a bit, but I'd like to explore a tree approach...
If we imagine an example where n = 3, we have to start with a `(`, and from there 
we can add on a `(` or `)`, etc. We need some kind of func where it can take the current
state of something and add one more thing to it. If it's the end, it can write a string

accumulation = "" (and gradually becomes "(" then "((" etc.)
state = {l:0, r:0} (and gradually becomes {l: 1, r:0} then {l:2, r:0} etc)
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def add(l=1, r=0, acc="("):
            if l == n and r == n: 
                res.append(acc)
            else:
                if l != n:
                    add(l + 1, r, acc + "(")
                if l != r:
                    add(l, r + 1, acc + ")")
        add()
        return res


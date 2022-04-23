"""
3/4

recurse((1,2,3), True, 0)
    recurse((2,3), False, 1) -> False
    recurse((1,3), False, 2) -> False
    recurse((1,2), False, 3) -> False

failed on 10/40

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True

        options = range(1, maxChoosableInteger + 1)

        if sum(options) < desiredTotal:
            return False

        @cache
        def recurse(choices, turn, total):
            if not choices: return False
            
            # can I win?
            if choices[-1] >= desiredTotal - total:
                return turn

            results = []
            for i in range(len(choices)):
                others = choices[:i] + choices[i+1:]
                results.append(recurse(others, not turn, total + choices[i]))
            return any(results)

        return recurse(tuple(options), True, 0)

Problem with mine is it doesn't introduce optimal play.

I had to read an answer to better get it but the gist is I was only playing optimally
at the last turn. 

            if choices[-1] >= desiredTotal - total:
                return turn

Choosing optimally really means trying all paths, which I was doing anyways, but
I was really just exploring all possible games, not all optimal games

I read some examples and found something that made sense to me.

Overall, I was trying to hard to think about it from both sides. Really if I had just
made a function that read 'can_win' instead of 'recurse', I would have been more inclined
to choose a better path.
"""

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True

        options = range(1, maxChoosableInteger + 1)

        if sum(options) < desiredTotal:
            return False

        @cache
        def can_win(choices, total):
            if not choices: return False
            
            # can I win?
            if choices[-1] >= desiredTotal - total:
                return True

            # have opponent play optimally...
            results = []
            for i, choice in enumerate(choices):
                others = choices[:i] + choices[i+1:]
                if can_win(others, total + choice):
                    # bad !
                    pass
                else:
                    return True
            return False

        return can_win(tuple(options), 0)

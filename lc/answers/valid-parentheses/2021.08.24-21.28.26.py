"""
I already sense that a stack is going to be very helpful here since
arbitrary degrees of nesting can occur. We also need to somehow match
the "same type of brackets". I think a map would do that quite easily.
We might be able to use ord() if say each matching pair were 1 more ord
value.

Let's go with the map idea though. Since it always opens and closes
in the same order, I suspect we'll only need a one way mapping.

For the stack, we can just use a python list.

The idea is that we'll append an item to the stack if it's an opening
symbol. If it's not an opening symbol, we'll pop the item from the stack
and compare it to the current symbol. If it's not the match, we return false.

Finally, we should be able to return True UNLESS there are any more items
in the stack, in which case that means there were brackets that were unmatched.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"{": "}", "(": ")", "[": "]"}
        stack = []

        # iterate through the string one char at a time and do logic described above
        for bracket in s:
            if bracket in mapping.keys():
                stack.append(bracket)
            else:
                if len(stack) == 0 or bracket != mapping[stack.pop()]:
                    return False

        # if there is anything stack, then return False also, else everything matched!
        return len(stack) == 0

"""
I failed my first submission because I failed to consider the edge case where
there were more right brackets than left. I handled the case where the were more
left brackets in the return statement, but for whatever reason I didn't get the inverse
edge case handled the first time around. Upon seeing the error, I immediately knew
what the issue was.
"""
        
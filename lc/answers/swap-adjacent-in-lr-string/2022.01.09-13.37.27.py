"""
first solution was:
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start == end:
            return True
        if len(start) == 1:
            return False

        results = []
        if start[0] == end[0]:
            results.append(self.canTransform(start[1:], end[1:]))
        if (start[:2] == "RX" and end[:2] == "XR") or (start[:2] == "XL" and end[:2] == "LX"):
            results.append(self.canTransform(start[2:], end[2:]))
        return any(results)

but didn't consider a case like 
"XXXXXLXXXX" -> "LXXXXXXXXX"

wrote this recursive solution but was still failing for some reason
class Solution:
    def canTransform(self, start: str, end: str, seen=set()) -> bool:
        if start in seen: return False
        seen.add(start)
        if start == end: return True
        if len(start) == 1: return False
        res = []
        for i in range(1, len(start)):
            if start[i-1:i+1] == "RX":
                res.append(self.canTransform(start[:i-1] + "XR" + start[i+1:], end, seen))
            if start[i-1:i+1] == "XL":
                res.append(self.canTransform(start[:i-1] + "LX" + start[i+1:], end, seen))
        return any(res)

this works but TLE on XXRXXRXLXLXXRXRXLXXRXXLXXRXXLXXLXLRXLXRX, which isn't even that big
class Solution:
    def canTransform(self, start: str, end: str, seen=set()) -> bool:
        seen = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in seen:
                seen.add(node)
                if node == end: return True
                for i in range(1, len(node)):
                    pair = node[i-1:i+1]
                    if pair == "RX":
                        stack.append(node[:i-1] + "XR" + node[i+1:])
                    if pair == "XL":
                        stack.append(node[:i-1] + "LX" + node[i+1:])
        return False


SO obviously there is an EXPLOSION of possibilities 
Let's think of a better way...
Really if you look at this string, you can think of the L and the R as being able to move left
or right amongst X's.
Honestly, doesn't that mean that if the Rs and Ls are in the same order and frequency, it works?

fails on 
"LXXLXRLXXL"
"XLLXRXLXLX"

the issue is that you can only move the Ls and Rs one way. You can only move the Ls to the left
and Rs to the right. Go figure.

What if we have a two pointers, one on start, one on end.
start=0 end=0 if they are both the same advance both

This should work:
RXXLRXRXL 
XRLXXRRLX 
start=0 end=0
end=0 (X), we're looking for an X... means we can tolerate only X's until R
oof this is tedious
start=1, we found an X, swap them.. now should look like
XRXLRXRXL
XRLXXRRLX
end=2, we're looking for an L, means we can tolerate only X's until L

Actually, I think this approach works but it can be simplified conceptually...
if we go searching for an L, we can do that and eventually swap. If we encounter an R, it's bad.
But if we're looking for an R, we have to give up since we can't move an R back anyways.
This presumes a left->right iteration. So we're looking for X's or L's
if we're looking for an X, we gotta find an R to swap
if we're looking for an L, we gotta find an X to swap
if we have an R, it's gotta be equal

XRXLRXRXL 
XRLXXRRLX 

Finally! this works but it could be written better and more efficient
from collections import defaultdict
class Solution:
    def canTransform(self, start: str, end: str, seen=set()) -> bool:
        start = list(start)
        for i, char in enumerate(end):
            if char != start[i]:
                if char == "X":
                    j = i
                    while j < len(end) - 1 and start[j] == "R": j += 1
                    if char == start[j]:
                        start[i], start[j] = start[j], start[i]
                    else:
                        return False
                elif char == "L":
                    j = i
                    while j < len(end) - 1 and start[j] == "X": j += 1
                    if char == start[j]:
                        start[i], start[j] = start[j], start[i]
                    else:
                        return False
                else:
                    return False
        return True

This is a lot more optimal since it can use the last j position

from collections import defaultdict
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start, j, prev = list(start), 0, None
        for i, char in enumerate(end):
            if char != start[i]:
                if char == "X":
                    j = max(i, j) if prev == char else i
                    while j < len(end) - 1 and start[j] == "R":
                        j += 1
                    if char == start[j]:
                        start[i], start[j] = start[j], start[i]
                    else:
                        return False
                elif char == "L":
                    j = max(i, j) if prev == char else i
                    while j < len(end) - 1 and start[j] == "X":
                        j += 1
                    if char == start[j]:
                        start[i], start[j] = start[j], start[i]
                    else:
                        return False
                else:
                    return False
            prev = char
        return True

Finally read the answers in the discussion. I almost had the right idea. Really all we need
to do is get rid of the X's and assert they are the same. That's what I thought. BUT this doesn't work
because by doing that you're assuming that Ls and Rs can move left and right fluidly but that's not the
case. What I should've realized is that you can just compare the indices at that point. Even though
the chars are the same, the indices may be incompatible
LX
XL
doesn't work although without X's, L == L, index of top L can't be less than the bottom.
The inverse is true for Rs.
"""


from collections import defaultdict
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s = [(i, char) for i, char in enumerate(start) if char != "X"]
        e = [(i, char) for i, char in enumerate(end) if char != "X"]
        if len(e) != len(s):
            return False
        for (i, s_char), (j, e_char) in zip(s, e):
            if s_char != e_char:
                return False
            if s_char == "L" and i < j:
                return False
            if s_char == "R" and j < i:
                return False
        return True





"""
===== Initial Thoughts =====
"3[a]2[bc]"
use a stack
3 is a digit so hold it..
[ means add to stack
a is content
] means pop item from stack and do content that many times

same again for second half

3[a2[c]] = a + 2[c]... 3 times
3 is a digit... hold it
[ means pop it to stack
a is content
2 is digit tho, not a part of content
[ means pop the 2 to a stack
c is content...
hmm. what if we put alpha on stack as well and pop two...
] process it and put it back on stack? if there's length...?
[3, 'acc']
] we see the second closer
[3, 'acc'] => accaccacc

I think that makes sense


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 


""
digit_buffer="" str_buffer="" stack=[3, 'acc'] res=""

Thought my solution was okay. not elegant but still ok. Unfortunately it doesn't pass
cases outside the base case.

stack=["abccdcdcd"]
"abc3[cd]xyz"

"]"
stack=[3, "a", "cc"] str_buffer="" digit_buffer=""

Ok, I'm just failing this one rather badly at this point. I'm going to look at the discussions.


class Solution:
    def decodeString(self, s: str) -> str:
        stack, digit_buffer, str_buffer = [], "", ""
        for char in s:
            if char == "[":
                if str_buffer: stack.append(str_buffer)
                stack.append(int(digit_buffer))
                digit_buffer, str_buffer = "", ""
            elif char == "]":
                if str_buffer: stack.append(str_buffer)
                str_buffer = ""
                s, quant = stack.pop(), stack.pop()
                substr = s * quant
                if stack:
                    stack[-1] += substr
                else:
                    stack.append(substr)
            else:
                if char.isdigit():
                    digit_buffer += char
                else:
                    str_buffer += char
        return "".join(stack) + str_buffer

so looking at https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
it's pretty clear I was on the right track and nearly there. 

"]]"
stack=["", 3] num=0 curr="c"
accaccacc
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack, num, curr = [], 0, ""
        for char in s:
            if char == "[":
                stack.append(curr)
                stack.append(num)
                num, curr = 0, ""
            elif char == "]":
                count, prev = stack.pop(), stack.pop()
                curr = prev + (curr * count)
            elif char.isdigit():
                num = (10 * num) + int(char)
            else:
                curr += char
        return curr



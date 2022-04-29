"""
===== Initial Thoughts =====
my immediate thought is that changing a 1 to 0 or visa versa can spiral

so here, we want to change that but one way the answer is 2
the other way the answer is much larger
10010101010
Now 2 just happens to be the number of chars that are bad...

But there are 6 bads here, yet it only requires changing 3, 000000

10101

10010101010 or shorter 100101
1001010. Once we arrive at a point like index 2, we can either change
it and continue right, or change the previous and continue right and left

Since this is an easy problem, I'm probably overthinking it.

=== Brute Force Approach ===
BFS
10010101010
10011101010

10011010101
10101010101 change 2

10011010101
0101

~~Complexity Analysis
Time - O(2^n) since for each char we can go down two paths?
Space - O(n) but more if we add caching

from collections import deque
class Solution:

    def find_bad(self, s):
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                return i
        return -1

    def minOperations(self, s: str) -> int:
        queue = deque([s])
        seen = set()
        num_operations = -1

        while queue:
            num_operations += 1
            for _ in range(len(queue)):
                item = queue.popleft()
                if item in seen:
                    continue
                seen.add(item)
                bad_index = self.find_bad(item)
                if bad_index == -1:
                    return num_operations

                # change current
                new = "1" if item[bad_index] == "0" else "0"
                queue.append(item[:bad_index] + new + item[bad_index + 1:])
                queue.append(item[:bad_index - 1] + new + item[bad_index:])

But that TLE's and is clearly way too complicated for an Easy.

BUT........

What if we represented them as numbers instead?
10101... if we right shift and and, it should be 0
01010 
0101
101
010

10011010101
00110101010

000111
001110

1100
1000
0100
1011

010101001010
101010010100
111111011110
000000100001

1001010101
0010101010
1011111111
0100000000

1001010101
1111111111


=== Implemented Approach ===
So I read one hint and it occured to me...

"Think about how the final string will look like."

final string will be one of two things...

say we have 000000
final string will be
010101 or
101010

what's the min diff between the two?

~~Complexity Analysis
Time - O(n)
Space - O(n)
"""
class Solution:
    def minOperations(self, s: str) -> int:
        N = len(s)
        final_1 = "".join(["1" if i % 2 == 0 else "0" for i in range(N)])
        final_2 = "".join(["0" if i % 2 == 0 else "1" for i in range(N)])
        diff_1 = diff_2 = 0
        for i in range(len(s)):
            diff_1 += s[i] != final_1[i]
            diff_2 += s[i] != final_2[i]
        return min(diff_1, diff_2)

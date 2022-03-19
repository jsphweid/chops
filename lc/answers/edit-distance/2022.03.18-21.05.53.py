"""
===== Initial Thoughts =====
I remember trying the graph solution last time but I don't think it worked out...
Let's just BFS again and see what happens :grimacing

        if not word1: return len(word2)
        if not word2: return len(word1)
        word2_len = len(word2)
        res = -1
        seen = set()
        queue = deque([(word1, len(word1), 0, 0)])
        while queue:
            res += 1
            for _ in range(len(queue)):
                word, l, i, j = queue.popleft()

                while i < l and j < word2_len and word[i] == word2[j]:
                    i += 1
                    j += 1

                if i == l and j == word2_len:
                    return res
                
                # insert
                if j != word2_len:
                    queue.append((word[:i] + word2[j] + word[i:], l + 1, i + 1, j + 1))

                # update
                if j != word2_len:
                    queue.append((word[:i] + word2[j] + word[i + 1:], l, i + 1, j + 1))

                # delete
                queue.append((word[:i] + word[i + 1:], l - 1, i, j))

memory limit exceeded...
let's try recursion with caching because I just looked up the answer...
"""

@cache
def recurse(word1, word2):
    if not word1 and not word2:
        return 0
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)
    if word1[0] == word2[0]:
        return recurse(word1[1:], word2[1:])
    insert = 1 + recurse(word1, word2[1:])
    update = 1 + recurse(word1[1:], word2[1:])
    delete = 1 + recurse(word1[1:], word2)
    return min(insert, update, delete)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return recurse(word1, word2)
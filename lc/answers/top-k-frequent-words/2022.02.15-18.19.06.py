"""
===== Initial Thoughts =====
do a counts dict O(n)
make a reverse mapping of counts to words O(n)
make a list of lists of words at each count level O(nlogn)
sort within each level ??
then flatten O(n)

~~Complexity Analysis
Time - O(nlogn)?
Space - O(n)

from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        count_to_words = defaultdict(list)
        for word, count in counts.items():
            count_to_words[count].append(word)
        res = []
        for num in sorted(list(count_to_words.keys()), reverse=True):
            res.append(sorted(count_to_words[num]))
        res = [item for group in res for item in group]
        return res[:k]

=== Implemented Approach ===
so since we only need the top k, this usually indicates a heap is ideal

~~Complexity Analysis
Time - 
Space - 

["i","love","leetcode","i","love","coding"]
{
    i: 2
    love: 2
    leetcode: 1
    coding: 1
}

we could use a max heap like [(2, i),(2, love),(1, leetcode),(1, coding)]
and pop off k items.
But how do we keep them sorted? I think heapq can deal with strings... but they are in reverse
actually, since we negate values and use min heap, the string should fall right in line
"""
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        pairs = [(-v, k) for k, v in counts.items()]
        heapq.heapify(pairs)
        res = []
        for i in range(k):
            res.append(heapq.heappop(pairs)[1])
        return res





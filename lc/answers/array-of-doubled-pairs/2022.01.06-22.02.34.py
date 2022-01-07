"""
===== Initial Thoughts =====
[4,-2,2,-4]]
[-4, -2, 2, 4]
[3, 4, 6, 8]
{3: 0, 4: 0, 6: 0, 8:0}

~~Complexity Analysis
Time - 
Space - 

[4,-2,2,-4]
[2,4,-2,-4]
counts={2:1, 4:1, -2:1, -4:1}

[4,-2,2,-4]
[2,4,-2,-4]
counts={2:1, 4:0, -2:1, -4:1}
"""
from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        neg, pos, num_zeros = [], [], 0
        for item in arr:
            if item < 0:
                neg.append(item)
            elif item > 0:
                pos.append(item)
            num_zeros += 1

        if num_zeros & 1:
            return False

        neg.sort(reverse=True)
        pos.sort()
        lst = pos + neg

        counts = Counter(lst)
        for item in lst:
            double = item * 2
            item_count, double_count = counts[item], counts[double]
            if item_count > double_count:
                return False
            counts[double] -= counts[item]
            counts[item] = 0
        return True

"""
[2,1,2,1,1,1,2,2]
[1,1,1,1,2,2,2,2]
{1: 4, 2: 4}
"""
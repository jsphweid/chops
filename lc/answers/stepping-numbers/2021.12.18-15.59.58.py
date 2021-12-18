"""
0-9
10, 12, 21, 23, 32, 34, 43, 45
123 321
234 432
345 543
456 654
567 765
678 876
789 987
123456789

1, 12, 123, 1234, 12345
2, 23, 234, 2345
12321
12121212
1232121232

1 0/2 

0 -> 1
1 -> 0/2
2 -> 1/3
...
9 -> 8

['1', '2', '3'] -> ('4' or '2')
3001 (going above 4 digits is useless)
dealing with 4129

1, 1000000
999999, 1000000

1 2 3 4 5 6 7 8 9
{1}
rec(1, '1')
    rec(2, '12')
    rec(0, '10')
rec(2, '2')

rec(3, '3')

recursive
        max_digits = len(str(high))
        res = set()
        def recurse(node: int, path: str) -> None:
            num = int(path)
            if num >= low and num <= high:
                res.add(num)
            if len(path) == max_digits:
                return
            else:
                if node < 9: recurse(node + 1, path + str(node + 1))
                if node > 0: recurse(node - 1, path + str(node - 1))
        for i in range(0, 10):
            recurse(i, str(i))
        return sorted(res)

2. only store path as an int, not last num as int and path as string

1 10 12
13 % 10 => 3
"""

from collections import deque
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        res = [0] if low == 0 else []
        queue = deque(range(1, 10))
        while queue:
            num = queue.popleft()
            if num >= low and num <= high:
                res.append(num)
            if num < high:
                last = num % 10
                if last > 0: queue.append(num * 10 + last - 1)
                if last < 9: queue.append(num * 10 + last + 1)
        return res

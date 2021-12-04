"""
[0,3,2,4,4]

"""

from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = list(range(n))
        
        def find(num):
            nodes = []
            while uf[num] != num:
                nodes.append(num)
                num = uf[num]
            for n in nodes:  # compress
                uf[n] = num
            return num

        def union(num1, num2):
            x_num1, x_num2 = find(num1), find(num2)
            if x_num1 != x_num2:
                uf[x_num1] = uf[x_num2]
            find(num1)
            find(num2)

        for l, r in edges:
            union(l, r)

        return len(set([find(i) for i in range(n)]))

class Solution:
    def knightDialer(self, n: int) -> int:
        adj = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        @cache
        def recurse(node, num_left):
            if num_left == 0 or node == 5:
                return 1
            return sum([recurse(num, num_left - 1) for num in adj[node]])
        res = 0
        max_size = 10**9 + 7
        for i in range(10):
            res += recurse(i, n - 1)
        return (res % max_size) - (n != 1)

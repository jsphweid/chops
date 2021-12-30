"""
~~Complexity Analysis
Something like, O(n) where n is the number of nodes
Time - O(n)
Space - O(n)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen, res = set(), 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == "1" and (i, j) not in seen:
                    res += 1
                    queue = [(i, j)]
                    while queue:
                        node = queue.pop()
                        if node in seen: continue
                        seen.add(node)
                        for direction in [(0,1),(1,0),(0,-1),(-1,0)]:
                            nxt_i, nxt_j = node[0] + direction[0], node[1] + direction[1]
                            if 0 <= nxt_i < len(grid) and 0 <= nxt_j < len(grid[0]):
                                if grid[nxt_i][nxt_j] == "1":
                                    queue.append((nxt_i, nxt_j))
        return res

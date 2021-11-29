class UnionFind:
    def __init__(self):
        self._unions = []

    def find(self, node):
        # returns index of group the node belongs to
        for i, union in enumerate(self._unions):
            if node in union: return i
        return None

    def union(self, i1, i2):
        self._unions[i1] = self._unions[i1] | self._unions[i2]
        self._unions.pop(i2)

    def add(self, s):
        self._unions.append(s)
        return len(self._unions) - 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
        edges.sort()
        uf = UnionFind()
        total = 0

        for cost, i, j in edges:
            i_index = uf.find(i)
            j_index = uf.find(j)
            if i_index is None and j_index is None:
                # if they don't belong to group, union them and put them in
                uf.add({i, j})
                total += cost
            elif i_index is not None and j_index is None:
                # if one belongs, put the non-belonging one into the belonging group
                new_j_index = uf.add({j})
                uf.union(i_index, new_j_index)
                total += cost
            elif j_index is not None and i_index is None:
                new_i_index = uf.add({i})
                uf.union(j_index, new_i_index)
                total += cost
            elif i_index == j_index:
                # if they both belong to same, ignore
                continue
            else:
                # if they both belong to different, union
                uf.union(i_index, j_index)
                total += cost

        return total


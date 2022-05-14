class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        M, N = len(land), len(land[0])

        def explore_farm(i, j):
            # given we're on a farm coord
            pos = [i, j]
            while i < M and land[i][j] == 1:
                i += 1
            i -= 1
            while j < N and land[i][j] == 1:
                j += 1
            j -= 1
            return pos + [i, j]

        farms = []
        for i in range(M):
            for j in range(N):
                if land[i][j] == 1:
                    if i > 0 and land[i - 1][j] == 1:
                        continue
                    if j > 0 and land[i][j - 1] == 1:
                        continue
                    farms.append(explore_farm(i, j))
        return farms

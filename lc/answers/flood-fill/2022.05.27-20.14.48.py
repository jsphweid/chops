class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        stack = [[sr, sc]]
        color = image[sr][sc]
        if color == newColor:
            return image
        while stack:
            i, j = stack.pop()
            if image[i][j] == color:
                image[i][j] = newColor
                for change in [[1,0],[0,1],[-1,0],[0,-1]]:
                    ii = i + change[0]
                    jj = j + change[1]
                    if 0 <= ii < M and 0 <= jj < N and image[ii][jj] == color:
                        stack.append([ii, jj])
        return image
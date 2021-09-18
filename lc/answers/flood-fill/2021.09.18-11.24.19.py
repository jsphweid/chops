"""
We should be able to do this fairly easily with a queue
we'll just pop the coord off the queue, flood fill neighbors -- any new neighbors
that weren't flood filled will simply be added to the queue
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = [[sr, sc]]
        while len(queue):
            r, c = queue.pop(0)
            current_color = image[r][c]
            if current_color == newColor:
                continue
            image[r][c] = newColor
            if r - 1 >= 0 and image[r - 1][c] == current_color:
                queue.append([r - 1, c])
            if r + 1 < len(image) and image[r + 1][c] == current_color:
                queue.append([r + 1, c])
            if c - 1 >= 0 and image[r][c - 1] == current_color:
                queue.append([r, c - 1])
            if c + 1 < len(image[r]) and image[r][c + 1] == current_color:
                queue.append([r, c + 1])
        return image

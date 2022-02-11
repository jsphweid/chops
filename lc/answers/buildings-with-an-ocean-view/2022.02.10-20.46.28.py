class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res, tallest = [], 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > tallest:
                res.append(i)
                tallest = heights[i]
        res.reverse()
        return res

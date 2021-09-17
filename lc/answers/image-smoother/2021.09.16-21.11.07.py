"""
this should work if we carefully consider the ranges, putting the valid boxes into a list
and averaging them.
"""

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result = []
        for i, row in enumerate(img):
            new_row = []
            for j, val in enumerate(row):
                points_to_average = []

                # add val
                points_to_average.append(val)
                # add val top left
                if i - 1 >= 0 and j - 1 >= 0:
                    points_to_average.append(img[i - 1][j - 1])
                # add val top
                if i - 1 >= 0:
                    points_to_average.append(img[i - 1][j])
                # add val top right
                if i - 1 >= 0 and j + 1 < len(row):
                    points_to_average.append(img[i - 1][j + 1])
                # add val left
                if j - 1 >= 0:
                    points_to_average.append(img[i][j - 1])
                # add val right
                if j + 1 < len(row):
                    points_to_average.append(img[i][j + 1])
                # add val bottom left
                if i + 1 < len(img) and j - 1 >= 0:
                    points_to_average.append(img[i + 1][j - 1])
                # add val bottom
                if i + 1 < len(img):
                    points_to_average.append(img[i + 1][j])
                # add val bottom right
                if i + 1 < len(img) and j + 1 < len(row):
                    points_to_average.append(img[i + 1][j + 1])


                new_row.append(int(sum(points_to_average) / len(points_to_average)))
            result.append(new_row)
        return result
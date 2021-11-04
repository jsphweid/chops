class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        coords = []
        for i in range(rows):
            for j in range(cols):
                coords.append([i, j])
        def sort_fn(coord):
            x, y = coord
            return abs(y - cCenter) + abs(x - rCenter)
        coords.sort(key=sort_fn)
        return coords

def is_valid(maze, i, j):
    m, n = len(maze), len(maze[0])
    return i > -1 and j > -1 and i != m and j != n and maze[i][j] == 0

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue, directions, seen = [(tuple(start), None)], [(1,0),(0,1),(-1,0),(0,-1)], set()
        dest = tuple(destination)
        while queue:
            position, direction = queue.pop()
            if direction:
                next_i, next_j = direction[0] + position[0], direction[1] + position[1]
                if is_valid(maze, next_i, next_j):
                    queue.append(((next_i, next_j), direction))
                else:
                    queue.append((position, None))
            else:
                if position == dest:
                    return True
                if position in seen:
                    continue
                seen.add(position)
                for i, j in directions:
                    next_i, next_j = i + position[0], j + position[1]
                    if is_valid(maze, next_i, next_j):
                        queue.append(((next_i, next_j), (i, j)))
        return False
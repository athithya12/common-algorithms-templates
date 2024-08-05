from typing import List, Tuple
from collections import deque


def bfs(grid: List[List[int]], start: Tuple[int, int]) -> List[Tuple[int, int]]:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([start])
    result = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        x, y = queue.popleft()
        if (x, y) not in visited:
            visited.add((x, y))
            result.append((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and (nx, ny) not in visited
                    and grid[nx][ny] == 1
                ):
                    queue.append((nx, ny))

    return result


# Example usage:
if __name__ == "__main__":
    grid = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 1], [0, 1, 1, 0, 1], [1, 0, 1, 1, 1]]
    start_point = (0, 0)
    print("BFS traversal starting from point", start_point, ":", bfs(grid, start_point))

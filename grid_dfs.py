from typing import List, Tuple


def dfs(grid: List[List[int]], start: Tuple[int, int]) -> List[Tuple[int, int]]:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    result = []

    def _dfs(x: int, y: int):
        if (x, y) not in visited:
            visited.add((x, y))
            result.append((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and (nx, ny) not in visited
                    and grid[nx][ny] == 1
                ):
                    _dfs(nx, ny)

    _dfs(start[0], start[1])
    return result


# Example usage:
if __name__ == "__main__":
    grid = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 1], [0, 1, 1, 0, 1], [1, 0, 1, 1, 1]]
    start_point = (0, 0)
    print("DFS traversal starting from point", start_point, ":", dfs(grid, start_point))

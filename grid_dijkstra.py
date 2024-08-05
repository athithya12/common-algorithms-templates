from typing import List, Tuple, Dict
import heapq


def dijkstra_grid(grid: List[List[int]], start: Tuple[int, int]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < rows and 0 <= y < cols

    # Priority queue to store (distance, x, y)
    priority_queue = [(0, start[0], start[1])]
    # Distance matrix initialized to infinity
    distances = [[float("inf")] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0

    while priority_queue:
        current_distance, x, y = heapq.heappop(priority_queue)

        if current_distance > distances[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                distance = current_distance + grid[nx][ny]
                if distance < distances[nx][ny]:
                    distances[nx][ny] = distance
                    heapq.heappush(priority_queue, (distance, nx, ny))

    return distances


# Example usage:
if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    start = (0, 0)
    shortest_distances = dijkstra_grid(grid, start)
    print("Shortest distances from start:", shortest_distances)

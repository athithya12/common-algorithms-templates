from typing import List, Tuple, Dict
import heapq


def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    # Priority queue to store (distance, node)
    priority_queue = [(0, start)]
    # Dictionary to store the shortest distance to each node
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage:
if __name__ == "__main__":
    graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
    start_node = 0
    shortest_distances = dijkstra(graph, start_node)
    print("Shortest distances from node", start_node, ":", shortest_distances)

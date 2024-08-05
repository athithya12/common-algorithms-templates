from typing import List, Dict, Tuple, Union


def bellman_ford(
    graph: Dict[int, List[Tuple[int, int]]], start: int
) -> Union[Dict[int, float], str]:
    # Initialize distances from start vertex to all vertices as infinity
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    # Relax edges up to (V-1) times where V is the number of vertices
    vertices = list(graph.keys())
    for _ in range(len(vertices) - 1):
        for u in vertices:
            for v, weight in graph[u]:
                if (
                    distances[u] != float("inf")
                    and distances[u] + weight < distances[v]
                ):
                    distances[v] = distances[u] + weight

    # Check for negative weight cycles
    for u in vertices:
        for v, weight in graph[u]:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                return "Graph contains a negative weight cycle"

    return distances


# Example usage:
if __name__ == "__main__":
    graph = {0: [(1, 4), (2, 1)], 1: [(2, 2), (3, 5)], 2: [(1, 2), (3, 8)], 3: []}
    start_node = 0
    distances = bellman_ford(graph, start_node)
    if isinstance(distances, str):
        print(distances)  # If a negative weight cycle is detected
    else:
        print("Shortest distances from node", start_node, ":", distances)

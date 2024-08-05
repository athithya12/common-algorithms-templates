from typing import List, Dict, Tuple, Union


def floyd_warshall(
    graph: Dict[int, Dict[int, int]]
) -> Tuple[Dict[int, Dict[int, Union[int, float]]], Dict[int, Dict[int, int]]]:
    # Extract all vertices
    vertices = set(graph.keys())
    for edges in graph.values():
        vertices.update(edges.keys())

    # Initialize distance and next matrices
    distance = {u: {v: float("inf") for v in vertices} for u in vertices}
    next_node = {u: {v: None for v in vertices} for u in vertices}

    # Set distance from a vertex to itself as 0
    for u in vertices:
        distance[u][u] = 0

    # Set initial distances based on graph
    for u in graph:
        for v, w in graph[u].items():
            distance[u][v] = w
            next_node[u][v] = v

    # Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_node[i][j] = next_node[i][k]

    # Check for negative weight cycles
    for u in vertices:
        if distance[u][u] < 0:
            return distance, "Graph contains a negative weight cycle"

    return distance, next_node


def construct_path(
    next_node: Dict[int, Dict[int, int]], start: int, end: int
) -> List[int]:
    path = []
    if next_node[start][end] is None:
        return path
    while start != end:
        path.append(start)
        start = next_node[start][end]
    path.append(end)
    return path


# Example usage:
if __name__ == "__main__":
    graph = {0: {1: 4, 2: 1}, 1: {2: 2, 3: 5}, 2: {1: 2, 3: 8}, 3: {}}
    distances, next_nodes = floyd_warshall(graph)

    if isinstance(distances, str):
        print(distances)  # If a negative weight cycle is detected
    else:
        print("Shortest distances:", distances)
        print("Next nodes for path reconstruction:", next_nodes)

        # Example path reconstruction
        start, end = 0, 3
        path = construct_path(next_nodes, start, end)
        print(f"Path from {start} to {end}:", path)

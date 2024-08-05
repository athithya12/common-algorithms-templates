from typing import List, Dict, Tuple, Union
from collections import deque, defaultdict


def topological_sort(graph: Dict[int, List[int]]) -> Union[List[int], str]:
    # Step 1: Compute in-degrees of all vertices
    in_degree = {node: 0 for node in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Step 2: Collect all vertices with in-degree of 0
    zero_in_degree = deque([node for node in in_degree if in_degree[node] == 0])

    # Step 3: Initialize the result list
    topo_order = []

    # Step 4: Process nodes
    while zero_in_degree:
        u = zero_in_degree.popleft()
        topo_order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                zero_in_degree.append(v)

    # Step 5: Check if the topological sort includes all vertices
    if len(topo_order) == len(graph):
        return topo_order
    else:
        return "Graph has a cycle and cannot be topologically sorted"


# Example usage:
if __name__ == "__main__":
    graph = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1]}
    topo_order = topological_sort(graph)
    if isinstance(topo_order, str):
        print(topo_order)  # If a cycle is detected
    else:
        print("Topological Sort:", topo_order)

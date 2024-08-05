from typing import List, Tuple, Dict
import heapq


def prim(
    graph: Dict[int, List[Tuple[int, int]]], start: int
) -> List[Tuple[int, int, int]]:
    # Priority queue to store (weight, node1, node2)
    priority_queue = []
    # Set to keep track of added nodes
    in_mst = set()
    # List to store the edges in the MST
    mst_edges = []

    # Start with the starting node
    in_mst.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(priority_queue, (weight, start, neighbor))

    while priority_queue:
        weight, node1, node2 = heapq.heappop(priority_queue)

        if node2 not in in_mst:
            in_mst.add(node2)
            mst_edges.append((node1, node2, weight))

            for neighbor, edge_weight in graph[node2]:
                if neighbor not in in_mst:
                    heapq.heappush(priority_queue, (edge_weight, node2, neighbor))

    return mst_edges


# Example usage:
if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (2, 2), (3, 5)],
        2: [(0, 1), (1, 2), (3, 8)],
        3: [(1, 5), (2, 8)],
    }
    start_node = 0
    mst_edges = prim(graph, start_node)
    print("Edges in the Minimum Spanning Tree:", mst_edges)

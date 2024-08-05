from typing import List, Dict, Set
from collections import deque


def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result


# Example usage:
if __name__ == "__main__":
    graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 4], 3: [1, 4], 4: [1, 2, 3]}
    start_node = 0
    print("BFS traversal starting from node", start_node, ":", bfs(graph, start_node))

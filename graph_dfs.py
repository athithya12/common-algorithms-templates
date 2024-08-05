from typing import List, Dict


def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    result = []

    def _dfs(node: int):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                _dfs(neighbor)

    _dfs(start)
    return result


# Example usage:
if __name__ == "__main__":
    graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 4], 3: [1, 4], 4: [1, 2, 3]}
    start_node = 0
    print("DFS traversal starting from node", start_node, ":", dfs(graph, start_node))

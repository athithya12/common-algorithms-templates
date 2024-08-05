from typing import List, Tuple, Dict


def tarjan_find_bridges(graph: Dict[int, List[int]]) -> List[Tuple[int, int]]:
    n = len(graph)  # Number of vertices
    ids = [-1] * n  # To store the id of each node
    low = [-1] * n  # To store the lowest id reachable
    visited = [False] * n
    bridges = []
    id_counter = [0]  # Mutable counter to keep track of the current id

    def dfs(at: int, parent: int) -> None:
        visited[at] = True
        ids[at] = low[at] = id_counter[0]
        id_counter[0] += 1

        for to in graph[at]:
            if to == parent:
                continue
            if not visited[to]:
                dfs(to, at)
                low[at] = min(low[at], low[to])
                if ids[at] < low[to]:
                    bridges.append((at, to))
            else:
                low[at] = min(low[at], ids[to])

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)

    return bridges


# Example usage:
if __name__ == "__main__":
    graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1, 4], 4: [3]}

    bridges = tarjan_find_bridges(graph)
    print("Bridges in the graph:", bridges)
    # Output: Bridges in the graph: [(3, 4), (1, 3)]

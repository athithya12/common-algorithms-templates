from typing import List, Dict, Set


def kosaraju(graph: Dict[int, List[int]]) -> List[Set[int]]:
    def dfs(v: int, visited: Set[int], stack: List[int]) -> None:
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(v)

    def reverse_graph(graph: Dict[int, List[int]]) -> Dict[int, List[int]]:
        reversed_graph = {u: [] for u in graph}
        for u in graph:
            for v in graph[u]:
                reversed_graph[v].append(u)
        return reversed_graph

    def fill_order(graph: Dict[int, List[int]]) -> List[int]:
        visited = set()
        stack = []
        for vertex in graph:
            if vertex not in visited:
                dfs(vertex, visited, stack)
        return stack

    def dfs_reverse(
        v: int,
        visited: Set[int],
        component: Set[int],
        transposed_graph: Dict[int, List[int]],
    ) -> None:
        visited.add(v)
        component.add(v)
        for neighbor in transposed_graph[v]:
            if neighbor not in visited:
                dfs_reverse(neighbor, visited, component, transposed_graph)

    # Step 1: Order vertices by finish time in decreasing order
    stack = fill_order(graph)

    # Step 2: Transpose the graph
    transposed_graph = reverse_graph(graph)

    # Step 3: Perform DFS on the transposed graph in the order of the stack
    visited = set()
    sccs = []
    while stack:
        v = stack.pop()
        if v not in visited:
            component = set()
            dfs_reverse(v, visited, component, transposed_graph)
            sccs.append(component)

    return sccs


# Example usage:
if __name__ == "__main__":
    graph = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [5, 7], 5: [6], 6: [4, 7], 7: []}

    sccs = kosaraju(graph)
    print("Strongly Connected Components:", sccs)
    # Output: Strongly Connected Components: [{0, 1, 2}, {3}, {4, 5, 6}, {7}]

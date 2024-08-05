from typing import List, Dict


def find_eulerian_circuit(graph: Dict[int, List[int]]) -> List[int]:
    def remove_edge(u: int, v: int):
        graph[u].remove(v)
        graph[v].remove(u)

    def hierholzer(u: int, circuit: List[int]):
        while graph[u]:
            v = graph[u][-1]
            remove_edge(u, v)
            hierholzer(v, circuit)
        circuit.append(u)

    # Find a vertex with a non-zero degree to start
    start_vertex = next((v for v in graph if graph[v]), None)

    if start_vertex is None:
        return []

    circuit = []
    hierholzer(start_vertex, circuit)
    return circuit[::-1]


# Example usage:
if __name__ == "__main__":
    # Example graph in adjacency list form
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4], 4: [2, 3]}

    circuit = find_eulerian_circuit(graph)
    print(f"Eulerian circuit: {circuit}")
    # Output: Eulerian circuit: [0, 2, 4, 3, 2, 1, 0]

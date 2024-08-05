from typing import List


def max_bipartite_matching(graph: List[List[int]]) -> int:
    # Helper function to find if a matching for vertex u is possible
    def bpm(u: int, seen: List[bool]) -> bool:
        # Try to find a match for vertex u
        for v in range(len(graph[0])):
            # If there is an edge from u to v and v is not yet seen in this search
            if graph[u][v] and not seen[v]:
                seen[v] = True  # Mark v as seen
                # If v is not matched or previously matched vertex for v can find an alternate match
                if match_r[v] == -1 or bpm(match_r[v], seen):
                    match_r[v] = u  # Match u with v
                    return True
        return False

    match_r = [-1] * len(
        graph[0]
    )  # Initialize all vertices in the right set as unmatched
    result = 0  # Count of matches found

    # Try to find a match for each vertex in the left set
    for i in range(len(graph)):
        seen = [False] * len(
            graph[0]
        )  # Mark all vertices in the right set as not seen for this search
        if bpm(i, seen):  # If a match is found
            result += 1  # Increment the result

    return result


# Example usage:
if __name__ == "__main__":
    # Example bipartite graph in adjacency matrix form
    # graph[u][v] = 1 if there is an edge from u in U to v in V, otherwise 0
    graph = [
        [
            0,
            1,
            1,
            0,
            0,
            0,
        ],  # Edges from vertex 0 in the left set to vertices 1 and 2 in the right set
        [
            1,
            0,
            0,
            1,
            0,
            0,
        ],  # Edges from vertex 1 in the left set to vertices 0 and 3 in the right set
        [
            0,
            0,
            1,
            0,
            0,
            0,
        ],  # Edge from vertex 2 in the left set to vertex 2 in the right set
        [
            0,
            0,
            1,
            1,
            0,
            0,
        ],  # Edges from vertex 3 in the left set to vertices 2 and 3 in the right set
        [
            0,
            0,
            0,
            0,
            1,
            1,
        ],  # Edges from vertex 4 in the left set to vertices 4 and 5 in the right set
        [
            0,
            0,
            0,
            0,
            0,
            1,
        ],  # Edge from vertex 5 in the left set to vertex 5 in the right set
    ]

    print(f"Maximum bipartite matching: {max_bipartite_matching(graph)}")  # Output: 4

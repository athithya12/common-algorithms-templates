from typing import List, Dict


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False  # They are already in the same set

        # Union by rank
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True


# Example usage:
if __name__ == "__main__":
    uf = UnionFind(10)  # Create 10 disjoint sets

    # Example unions
    print(uf.union(1, 2))  # Union of set containing 1 and set containing 2
    print(
        uf.union(2, 3)
    )  # Union of set containing 2 (which now contains 1) and set containing 3
    print(uf.union(4, 5))  # Union of set containing 4 and set containing 5
    print(
        uf.union(1, 5)
    )  # Union of set containing 1 (which now contains 2, 3) and set containing 5 (which now contains 4)

    # Example finds
    print(uf.find(1))  # Should print the representative of the set containing 1
    print(uf.find(3))  # Should print the same representative as find(1)
    print(uf.find(4))  # Should print the representative of the set containing 4
    print(uf.find(5))  # Should print the same representative as find(4)

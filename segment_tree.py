from typing import List


class SegmentTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data: List[int]):
        # Initialize leaves
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, value: int):
        # Set value at position index
        index += self.n
        self.tree[index] = value
        # Update the tree
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def query(self, left: int, right: int) -> int:
        # Query the sum in the interval [left, right)
        left += self.n
        right += self.n
        result = 0
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result


# Example usage:
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(data)

    print("Sum of range [1, 4):", seg_tree.query(1, 4))  # Output: 15 (3 + 5 + 7)

    seg_tree.update(2, 6)
    print(
        "Sum of range [1, 4) after update:", seg_tree.query(1, 4)
    )  # Output: 16 (3 + 6 + 7)

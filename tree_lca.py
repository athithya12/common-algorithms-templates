class TreeNode:
    def __init__(self, value: int, parent: "TreeNode" = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


def find_depth(node: TreeNode) -> int:
    depth = 0
    while node:
        node = node.parent
        depth += 1
    return depth


def lca_with_parent_pointers(node1: TreeNode, node2: TreeNode) -> TreeNode:
    # Find depths of both nodes
    depth1 = find_depth(node1)
    depth2 = find_depth(node2)

    # Equalize the depths
    while depth1 > depth2:
        node1 = node1.parent
        depth1 -= 1

    while depth2 > depth1:
        node2 = node2.parent
        depth2 -= 1

    # Find the common ancestor
    while node1 != node2:
        node1 = node1.parent
        node2 = node2.parent

    return node1


def lca(
    root: Optional[TreeNode], node1: TreeNode, node2: TreeNode
) -> Optional[TreeNode]:
    if root is None:
        return None

    # If either node1 or node2 matches the root, report the match up.
    if root == node1 or root == node2:
        return root

    # Recur for the left and right subtrees.
    left_lca = lca(root.left, node1, node2)
    right_lca = lca(root.right, node1, node2)

    # If both calls return non-None, this node is the LCA.
    if left_lca and right_lca:
        return root

    # Otherwise, return the non-None child.
    return left_lca if left_lca is not None else right_lca


# Example usage
if __name__ == "__main__":
    # Construct the tree
    root = TreeNode(1)
    root.left = TreeNode(2, root)
    root.right = TreeNode(3, root)
    root.left.left = TreeNode(4, root.left)
    root.left.right = TreeNode(5, root.left)
    root.right.left = TreeNode(6, root.right)
    root.right.right = TreeNode(7, root.right)

    node1 = root.left.left  # Node 4
    node2 = root.left.right  # Node 5

    ancestor = lca_with_parent_pointers(node1, node2)
    if ancestor:
        print(
            f"The LCA of node {node1.value} and node {node2.value} is node {ancestor.value}"
        )
    else:
        print("No common ancestor found.")

class ListNode:
    def __init__(self, value: int, next: "ListNode" = None):
        self.value = value
        self.next = next


def find_cycle_start(head: ListNode) -> ListNode:
    if not head:
        return None

    slow = head
    fast = head

    # Phase 1: Detect if a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None  # No cycle detected

    # Phase 2: Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# Example usage:
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    #                           ^              |
    #                           |              v
    #                           6 <- 7 <- 8 <- 9
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)

    # Link nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node6  # Creating a cycle

    # Find cycle start
    cycle_start_node = find_cycle_start(node1)
    if cycle_start_node:
        print("Start of cycle is:", cycle_start_node.value)  # Output: 6
    else:
        print("No cycle detected.")

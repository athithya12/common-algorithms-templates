from collections import deque


def monotonic_queue_max(arr, window_size):
    # Deque to store indices of elements, in decreasing order
    dq = deque()

    # Result array to store the maximum of each sliding window
    result = []

    # Traverse the array
    for i in range(len(arr)):
        # Remove elements from the back of the deque if they are smaller than the current element
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        # Add the current element index to the deque
        dq.append(i)

        # Remove elements from the front if they are outside the window
        if dq[0] < i - window_size + 1:
            dq.popleft()

        # Once we've processed at least 'window_size' elements, the front of the deque is the max
        if i >= window_size - 1:
            result.append(arr[dq[0]])

    return result

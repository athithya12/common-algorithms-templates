def monotonic_stack(arr):
    # Stack to store indices (can store values directly as needed)
    stack = []

    # Result array (if you need to store some output, like next greater or smaller element)
    result = [-1] * len(arr)  # Initialize based on problem's requirement

    # Traverse through each element
    for i in range(len(arr)):
        # Maintain the monotonic property (increasing or decreasing)
        while stack and arr[stack[-1]] < arr[i]:
            # Stack is popped when the current element is greater than the top
            index = stack.pop()

            # Do something with this popped element, e.g., store the result
            result[index] = arr[
                i
            ]  # Example: arr[i] is the next greater element for arr[index]

        # Push current index onto the stack
        stack.append(i)

    # If the problem requires post-processing for elements that don't have a result
    while stack:
        index = stack.pop()
        result[index] = -1  # Example: no next greater element exists

    return result

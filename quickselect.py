from typing import List


def quickselect(arr: List[int], k: int) -> int:
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]  # Change to > for largest
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]  # Change to < for largest

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return quickselect(right, k - len(left) - len(middle))


# Example usage:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    for target_index in range(len(arr)):
        print(f"{target_index}-th smallest element is:", quickselect(arr, target_index))

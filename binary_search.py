def bisect_left(a, x, lo=0, hi=None):
    while lo < hi:
        mid = (lo + hi) // 2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_left(a, x, lo=0, hi=None):
    while lo < hi:
        mid = (lo + hi) // 2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if a[mid] < x:
            hi = mid
        else:
            lo = mid + 1
    return lo

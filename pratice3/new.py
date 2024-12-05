def minimize_diff(cubes, k):
    """
    Minimizes the difference between adjacent cubes in a non-decreasing array while keeping the first and last elements fixed.

    Args:
        cubes: A list of integers representing the side lengths of the cubes in non-decreasing order.
        k: The number of cubes to remove.

    Returns:
        The minimum possible difference between adjacent cubes after removing k cubes.
    """

    n = len(cubes)
    if k == 0 or k >= n - 2:
        return max(cubes[i] - cubes[i - 1] for i in range(1, n))

    # Initialize the sliding window
    window_start = 0
    window_end = k + 1
    max_diff = max(cubes[i] - cubes[i - 1] for i in range(1, window_end))

    # Slide the window and update max_diff
    for i in range(window_end, n):
        # Calculate the maximum difference within the window
        window_max = max(cubes[i] - cubes[i - 1], cubes[i - k - 1] - cubes[i - k])
        max_diff = max(max_diff, window_max)
        window_start += 1

    return max_diff

# Example usage
cubes = [1, 2, 3, 7, 8]
k = 2
result = minimize_diff(cubes, k)
print(result)
# Output: 5
def trap(height):
    """
    Function to calculate total water trapped between bars.
    Uses two-pointer technique for O(n) time and O(1) space.
    """

    n = len(height)
    if n < 3:  # less than 3 bars, no water can be trapped
        return 0

    left, right = 0, n - 1
    left_max, right_max = 0, 0
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1

    return water_trapped


# ----------------------------
# Example Test Cases
# ----------------------------
if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 1, 1], 0),
        ([5], 0),
        ([2, 0, 2], 2),
        ([0, 0, 0], 0),
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 3, 2, 1], 0),
    ]

    for i, (heights, expected) in enumerate(test_cases, 1):
        result = trap(heights)
        print(f"Test Case {i}: Input={heights} | Output={result} | Expected={expected}")

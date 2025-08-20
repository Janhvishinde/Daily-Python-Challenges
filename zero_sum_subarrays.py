from collections import defaultdict

def find_zero_sum_subarrays(arr):
    n = len(arr)
    prefix_sum = 0
    sum_map = defaultdict(list)   # Maps prefix_sum -> list of indices
    result = []

    for i in range(n):
        prefix_sum += arr[i]

        # Case 1: Subarray starts from index 0 to i
        if prefix_sum == 0:
            result.append((0, i))

        # Case 2: If prefix_sum was seen before, subarray from prev_index+1 to i is zero-sum
        if prefix_sum in sum_map:
            for start_index in sum_map[prefix_sum]:
                result.append((start_index + 1, i))

        # Store current index for this prefix_sum
        sum_map[prefix_sum].append(i)

    return result


# Example usage
if __name__ == "__main__":
    arr = [1, 2, -3, 3, -1, 2]
    print(find_zero_sum_subarrays(arr))  # Output: [(0, 2), (1, 3)]

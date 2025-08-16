def find_missing_number(arr):
    n = len(arr) + 1  # Since one number is missing
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum


# Test Cases
if __name__ == "__main__":
    print(find_missing_number([1, 2, 4, 5]))       # Output: 3
    print(find_missing_number([2, 3, 4, 5]))       # Output: 1
    print(find_missing_number([1, 2, 3, 4]))       # Output: 5
    print(find_missing_number([1]))                # Output: 2
    print(find_missing_number(list(range(1, 1000000))))  # Output: 1000000

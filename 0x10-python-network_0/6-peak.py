#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of integers.

    Returns:
        int: The peak element.

    Note:
        There may be more than one peak in the list.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]

# Complexity: O(log(n))

if __name__ == "__main__":
    # Test cases
    print(find_peak([1, 2, 4, 6, 3]))  # Output: 6
    print(find_peak([4, 2, 1, 2, 3, 1]))  # Output: 3
    print(find_peak([2, 2, 2]))  # Output: 2
    print(find_peak([]))  # Output: None
    print(find_peak([-2, -4, 2, 1]))  # Output: 2
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4

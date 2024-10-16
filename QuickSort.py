from typing import List, Any

def partition(arr: List[int], low: int, high: int) -> int:
    """Partition the array around a pivot."""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr: List[int], low: int, high: int, i: int) -> int:
    """Return the i-th smallest element in the array."""
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)
    k = pivot_index - low + 1  # Number of elements in the left partition

    if i == k:
        return arr[pivot_index]
    elif i < k:
        return quickselect(arr, low, pivot_index - 1, i)
    else:
        return quickselect(arr, pivot_index + 1, high, i - k)

def validate_input(arr: List[int], k: int) -> None:
    """Validate the input parameters."""
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("Input must be a list of integers.")
    if k < 1 or k > len(arr):
        raise IndexError("k is out of bounds. Must be between 1 and the length of the array.")

def find_kth_element(arr: List[int], k: int, order: str = 'smallest') -> Any:
    """Find the k-th smallest or largest element in the array."""
    validate_input(arr, k)

    if order == 'largest':
        k = len(arr) - k + 1  # Adjust k for largest
    return quickselect(arr.copy(), 0, len(arr) - 1, k)

def sort_array(arr: List[int]) -> List[int]:
    """Return a sorted version of the array."""
    return sorted(arr)

# Example usage:
arr = [3, 2, 1, 5, 4]
k_smallest = 3  # Find the 3rd smallest element
k_largest = 2   # Find the 2nd largest element

try:
    ith_smallest = find_kth_element(arr, k_smallest, order='smallest')
    ith_largest = find_kth_element(arr, k_largest, order='largest')

    print(f"The {k_smallest}rd smallest element is {ith_smallest}")
    print(f"The {k_largest}nd largest element is {ith_largest}")

    # Optional: Verify by sorting
    sorted_arr = sort_array(arr)
    print("Sorted array:", sorted_arr)

except (IndexError, ValueError) as e:
    print(e)

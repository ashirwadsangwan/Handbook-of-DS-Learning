def binarySearch(array, target):
    # Write your code here.
    n = len(array)
    left = 0
    right = n - 1

    return binary_search_helper(array, left, right, target)


def binary_search_helper(array, left, right, target):

    if left > right:
        return -1

    mid = (left + right) // 2

    if array[mid] == target:
        return mid

    elif array[mid] < target:
        # number is somewhere between mid and end of the array
        return binary_search_helper(array, mid + 1, right, target)

    elif array[mid] > target:
        # number lies in the first half of the list
        return binary_search_helper(array, left, mid - 1, target)

def minNum(arr, n):
    """Returns the minimum number from the array using recursion
    Base case:  if len(arr) is 1 then return arr[0]
                else return minimum of (n-1)th element and recursion output for n-1 elements
    Time: O(n) since in-built `max` function takes linear time to find the max element
    Space: O(1) since only one variable is created to store the max value while searching
    """

    if n == 1:
        return arr[0]
    else:
        return min(minNum(arr, n - 1), arr[n - 1])


def maxNum(arr, n):
    if n == 1:
        return arr[0]
    else:
        # the below block essentially is MAX(arr[n-1], arr[n-2],........., arr[0])
        return max(arr[n - 1], maxNum(arr, n - 1))


if __name__ == "__main__":
    arr = [1, 4, 45, 6, -50, 10, 2]
    n = len(arr)
    print(minNum(arr, n))
    print(maxNum(arr, n))

class Solution:
    # Time: O(n), Space: O(n)
    def fib(self, n: int) -> int:
        memo = [0 for _ in range(n + 1)]

        memo[0:2] = [0, 1]
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]

    # Time: O(2^n), Space: O(n)
    # the space required is proportional to the maximum depth of the recursion tree
    def fib2(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)

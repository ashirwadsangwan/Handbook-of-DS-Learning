# Time: O(n), Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for _ in range(n + 1)]

        memo[0:2] = [1, 2]
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n - 1]

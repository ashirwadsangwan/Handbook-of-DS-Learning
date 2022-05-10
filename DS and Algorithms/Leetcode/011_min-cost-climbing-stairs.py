from functools import cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        left = 0
        minCost = 0
        cost.append(0)
        print(cost)

        @cache
        def calCost(n):
            if n <= 1:
                return cost[n]
            else:
                return cost[n] + min(calCost(n - 1), calCost(n - 2))

        return calCost(len(cost) - 1)

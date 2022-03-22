# Time: O(n^2), Space: O(n)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = {}
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    ans = [nums[i], nums[left], nums[right]]
                    if str(ans) not in result:
                        result[str(ans)] = 1
                    else:
                        result[str(ans)] += 1

                    left += 1
                    right -= 1

                elif currentSum < 0:
                    left += 1

                elif currentSum > 0:
                    right -= 1

        return [eval(i) for i in result.keys()]

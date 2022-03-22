class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        nums.sort()
        out = None
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == target:
                    return currentSum

                if out == None or abs(target - currentSum) < abs(target - out):
                    out = currentSum

                if currentSum < target:
                    left += 1
                else:
                    right -= 1

        return out

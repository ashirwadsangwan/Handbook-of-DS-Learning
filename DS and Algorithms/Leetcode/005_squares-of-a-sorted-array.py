# Time: O(n), Space: O(n)

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums)-1
        index = -1
        out = [0]*len(nums)
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                out[index] = (nums[left]**2)
                left += 1
            else:
                out[index] = (nums[right]**2)
                right -= 1
            index -= 1
        return out
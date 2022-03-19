# Initial Approach
# Time: O(n), Space: (n)
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        num_dict = {} # saving in dict for faster search
        for i in range(len(nums)): 
            
            curr = target - nums[i] # searching the second number instead of iterating over both

            if curr in nums: # checking if the second number also exists in the array
                return [i, nums.index(curr)] 
            else:
                num_dict[nums[i]] = True

# Another approach could be iterating over the array twice which will have:
# Time: O(n^2), Space: O(1)

if __name__ == '__main__':
    nums = [2, 3, 1, 8, 19]
    target = 11

    assert Solution().twoSum(nums, target) == [2, 4] or [4, 2]
    print(f"Test passed: the matched indices are {Solution().twoSum(nums, target)}")




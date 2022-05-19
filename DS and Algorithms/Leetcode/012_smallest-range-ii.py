class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:

        """
        SORT the array and divide it into two parts:
        left half:(A[0]+k, A[1]+k, ..., A[i]+k)
                        |                      |
                possible minimum     possible maximum
                        |                      |
        right half:(A[i+1]-k, A[i+2]-k ..., A[SIZE-1]-k)

        min(initialMax-initialMax, max(maximums)-min(minimums))        
        
        """
        nums.sort()
        mi, ma = nums[0] + k, nums[-1] - k
        minScore = nums[-1] - nums[0]

        for i in range(len(nums) - 1):
            new_min = min(nums[i + 1] - k, mi)
            new_max = max(nums[i] + k, ma)
            minScore = min(minScore, new_max - new_min)

        return minScore

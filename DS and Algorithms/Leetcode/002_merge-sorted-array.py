class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 and m == 0:
            return []
        if n == 0:
            return nums1

        left = 0
        right = 0

        while left < m:
            if nums1[left] <= nums2[right]:
                left += 1

            elif nums1[left] > nums2[right]:
                temp = nums1[left]
                nums1[left] = nums2[right]
                nums2[right] = temp
                self.sort_check(nums2)
                left += 1

        while left < m + n:
            nums1[left] = nums2[right]
            right += 1
            left += 1

        print(nums1)

    def sort_check(self, nums):
        t = 0
        i = 1
        while i < len(nums) and nums[t] > nums[i]:
            temp = nums[i]
            nums[i] = nums[t]
            nums[t] = temp
            i += 1
            t += 1

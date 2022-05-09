class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersect = []
        from collections import Counter

        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        unique_nums = [key for key in dict1.keys() if key in dict2.keys()]

        for num in unique_nums:
            intersect += [num] * min(dict1[num], dict2[num])

        return intersect

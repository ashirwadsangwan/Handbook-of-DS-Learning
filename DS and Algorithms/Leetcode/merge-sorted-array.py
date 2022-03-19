class Solution:
    def merge(self, nums1: list(int), m: int, nums2: list(int), n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        right = 0

        out = []

        while left < len(nums1[:m])-1 and right < len(nums2[:n]) - 1 :
            if nums1[:m][left] == nums2[:n][right]:
                out.append(nums1[:m][left])
                left += 1
                out.append(nums2[:n][right])
                right += 1
            
            elif nums1[:m][left] < nums2[:n][right]:
                out.append(nums1[:m][left])
                left += 1

            elif nums1[:m][left] > nums2[:n][right]:
                out.append(nums2[:n][right])
                right += 1


def move_array_by_one(arr: list(int)) -> list(int):
    
"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。


示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = (nums1 + nums2)
        nums.sort()
        t = len(nums) // 2
        return nums[t] if len(nums) % 2 == 1 else (nums[t - 1] + nums[t]) / 2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1

        start = 0
        end = len1
        while start <= end:
            a = (start + end) // 2
            b = (len1 + len2 + 1) // 2 - a
            if a > 0 and nums1[a - 1] > nums2[b]:
                end = a - 1
            elif a < len1 and nums2[b - 1] > nums1[a]:
                start = a + 1
            else:
                if a == 0:
                    mid = nums2[b - 1]
                elif b == 0:
                    mid = nums1[a - 1]
                else:
                    mid = max(nums1[a - 1], nums2[b - 1])
                if (len1 + len2) % 2 == 1:
                    return mid
                else:
                    if a == len1:
                        return (mid + nums2[b]) / 2
                    elif b == len2:
                        return (mid + nums1[a]) / 2
                    else:
                        return (mid + min(nums1[a], nums2[b])) / 2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    print(Solution().findMedianSortedArrays2([1, 3], [2]))

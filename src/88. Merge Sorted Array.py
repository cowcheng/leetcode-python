# Author: Cow Cheng
# Date: 13-10-2022

"""
59 / 59 test cases passed.
Status: Accepted
Runtime: 36 ms
Memory Usage: 14 MB
"""

from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length_1 = len(nums1)
        end_m = 0
        end_n = 0
        while end_m < length_1:
            if end_m < m:
                end_m += 1
                continue
            if end_n < n:
                nums1[end_m] = nums2[end_n]
            end_m += 1
            end_n += 1
        nums1.sort()


print(Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(Solution().merge(nums1=[1], m=1, nums2=[], n=0))
print(Solution().merge(nums1=[0], m=0, nums2=[1], n=1))

# Author: Cow Cheng
# Date: 08-10-2022

"""
64 / 64 test cases passed.
Status: Accepted
Runtime: 121 ms
Memory Usage: 14.9 MB
"""

from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        for i in range(length):
            if target <= nums[i]:
                return i
        return length


print(Solution().searchInsert(nums=[1, 3, 5, 6], target=5))
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=7))

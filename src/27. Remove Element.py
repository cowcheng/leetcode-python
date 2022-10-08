# Author: Cow Cheng
# Date: 08-10-2022

"""
113 / 113 test cases passed.
Status: Accepted
Runtime: 62 ms
Memory Usage: 13.9 MB
"""

from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        while start < len(nums):
            if nums[start] == val:
                nums.remove(nums[start])
            else:
                start += 1
        return len(nums)


print(Solution().removeElement(nums=[3, 2, 2, 3], val=3))
print(Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))

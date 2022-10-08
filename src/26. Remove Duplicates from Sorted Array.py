# Author: Cow Cheng
# Date: 08-10-2022

"""
361 / 361 test cases passed.
Status: Accepted
Runtime: 369 ms
Memory Usage: 15.6 MB
"""

from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def removeDuplicates(self, nums: List[int]) -> int:
        dup_dict = {}
        start = 0
        change_pos = 0
        while start < len(nums):
            if nums[start] not in dup_dict:
                dup_dict[nums[start]] = 1
                start += 1
                change_pos += 1
            else:
                nums.remove(nums[start])
        return len(dup_dict)


print(Solution().removeDuplicates(nums=[1, 1, 2]))
print(Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

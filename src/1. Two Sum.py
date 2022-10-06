# Author: Cow Cheng
# Date: 06-10-2022

"""
57 / 57 test cases passed.
Status: Accepted
Runtime: 6607 ms
Memory Usage: 14.8 MB
"""

from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for a in range(length):
            result = target - nums[a]
            for b in range(length):
                if nums[b] == result and a != b:
                    return [a, b]


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[3, 2, 4], target=6))
print(Solution().twoSum(nums=[3, 3], target=6))

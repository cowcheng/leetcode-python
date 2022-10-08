# Author: Cow Cheng
# Date: 08-10-2022

"""
111 / 111 test cases passed.
Status: Accepted
Runtime: 86 ms
Memory Usage: 13.9 MB
"""

from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp_s = ''
        for d in digits:
            tmp_s = f'{tmp_s}{d}'
        result = int(tmp_s) + 1
        tmp_result = str(result)
        tmp_l = []
        for i in tmp_result:
            tmp_l.append(int(i))
        return tmp_l


print(Solution().plusOne(digits=[1, 2, 3]))
print(Solution().plusOne(digits=[4, 3, 2, 1]))
print(Solution().plusOne(digits=[9]))

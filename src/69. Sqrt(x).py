# Author: Cow Cheng
# Date: 08-10-2022

"""
1017 / 1017 test cases passed.
Status: Accepted
Runtime: 62 ms
Memory Usage: 13.8 MB
"""

import math


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))


print(Solution().mySqrt(x=4))
print(Solution().mySqrt(x=8))

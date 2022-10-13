# Author: Cow Cheng
# Date: 13-10-2022

"""
45 / 45 test cases passed.
Status: Accepted
Runtime: 33 ms
Memory Usage: 13.9 MB
"""


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def climbStairs(self, n: int) -> int:
        a, b, c = 0, 1, 2
        if n <= 2:
            return n
        while n > 2:
            a, b = b, c
            c = a + b
            n = n - 1
        return c


print(Solution().climbStairs(n=2))
print(Solution().climbStairs(n=3))

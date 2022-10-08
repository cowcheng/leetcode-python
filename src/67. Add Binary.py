# Author: Cow Cheng
# Date: 08-10-2022

"""
294 / 294 test cases passed.
Status: Accepted
Runtime: 34 ms
Memory Usage: 13.8 MB
"""


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def addBinary(self, a: str, b: str) -> str:
        a_bin = int(a, 2)
        b_bin = int(b, 2)
        result = str(bin(a_bin + b_bin))[2:]
        if result == '':
            return str(0)
        return result


print(Solution().addBinary(a='11', b='1'))
print(Solution().addBinary(a='1010', b='1011'))

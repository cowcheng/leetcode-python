# Author: Cow Cheng
# Date: 06-10-2022

"""
124 / 124 test cases passed.
Status: Accepted
Runtime: 82 ms
Memory Usage: 14 MB
"""

from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = 0
        if len(strs) == 1:
            return strs[0]
        while a <= len(strs[0]):
            pat = strs[0][:a]
            for i in range(1, len(strs)):
                if len(strs[i]) == 0:
                    return ''
                if not strs[i].startswith(pat):
                    return pat[:a - 1]
            a += 1
        return strs[0]


print(Solution().longestCommonPrefix(strs=['flower', 'flow', 'flight']))
print(Solution().longestCommonPrefix(strs=['dog', 'racecar', 'car']))

# Author: Cow Cheng
# Date: 06-10-2022

"""
3999 / 3999 test cases passed.
Status: Accepted
Runtime: 52 ms
Memory Usage: 13.9 MB
"""


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def romanToInt(self, s: str) -> int:
        romans_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        length = len(s)
        total = 0
        for i in range(length):
            if i == length - 1 or romans_dict[s[i]] >= romans_dict[s[i + 1]]:
                total += romans_dict[s[i]]
            else:
                total -= romans_dict[s[i]]
        return total


print(Solution().romanToInt(s='III'))
print(Solution().romanToInt(s='LVIII'))
print(Solution().romanToInt(s='MCMXCIV'))

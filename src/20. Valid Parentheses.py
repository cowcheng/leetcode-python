# Author: Cow Cheng
# Date: 06-10-2022

"""
92 / 92 test cases passed.
Status: Accepted
Runtime: 62 ms
Memory Usage: 14 MB
"""


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def isValid(self, s: str) -> bool:
        length = len(s)
        s_list = []
        for i in range(length):
            if s[i] == '(':
                s_list.append(')')
            elif s[i] == '[':
                s_list.append(']')
            elif s[i] == '{':
                s_list.append('}')
            else:
                if not s_list:
                    return False
                if s[i] == s_list[-1]:
                    s_list.pop()
                else:
                    return False
        if not s_list:
            return True
        else:
            return False


print(Solution().isValid(s='()'))
print(Solution().isValid(s='()[]{}'))
print(Solution().isValid(s='(]'))

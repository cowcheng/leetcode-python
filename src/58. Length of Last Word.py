# Author: Cow Cheng
# Date: 08-10-2022

"""
58 / 58 test cases passed.
Status: Accepted
Runtime: 66 ms
Memory Usage: 14 MB
"""


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def lengthOfLastWord(self, s: str) -> int:
        text_list = s.split(' ')
        last = len(text_list) - 1
        while last > 0:
            if text_list[last] != '':
                break
            last -= 1
        return len(text_list[last])


print(Solution().lengthOfLastWord(s='Hello World'))
print(Solution().lengthOfLastWord(s='   fly me   to   the moon  '))
print(Solution().lengthOfLastWord(s='luffy is still joyboy'))

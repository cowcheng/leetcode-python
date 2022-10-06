# Author: Cow Cheng
# Date: 06-10-2022

"""
11510 / 11510 test cases passed.
Status: Accepted
Runtime: 125 ms
Memory Usage: 13.8 MB
"""


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def isPalindrome(self, x: int) -> bool:
        txt = list(str(x))
        start = 0
        end = len(txt) - 1
        while start < end:
            new_txt = txt.copy()
            tmp = new_txt[start]
            new_txt[start] = new_txt[end]
            new_txt[end] = tmp
            if txt != new_txt:
                return False
            start += 1
            end -= 1
        return True


print(Solution().isPalindrome(x=121))
print(Solution().isPalindrome(x=-121))
print(Solution().isPalindrome(x=10))

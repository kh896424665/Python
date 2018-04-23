"""
回文数即将一个数字倒序和原来数字一样，负数没有回文数
"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = 0
        t = x
        if x < 0:
            return False
        while x != 0:
            a = x % 10
            x = x // 10
            y = y * 10 + a
        if y < -2**31 or y > 2 ** 31 -1:
            return False
        if t == y:
            return True
        else:
            return False


pal = Solution()
print(pal.isPalindrome(-2147447412))

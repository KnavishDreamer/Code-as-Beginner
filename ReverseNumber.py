class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = abs(x)
        rev = 0
        while y > 0:
            rem = y % 10
            rev = 10 *rev + rem
            y = y // 10
        
        if x < 0:
            rev = -rev
        return rev

a = Solution()
print a.reverse(-100056)

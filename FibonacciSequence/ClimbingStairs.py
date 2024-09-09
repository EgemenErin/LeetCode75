class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num1 = 1
        num2 = 1
        for i in range(n-1):
            temp = num1
            num1 = num1 + num2
            num2 = temp

        return num1
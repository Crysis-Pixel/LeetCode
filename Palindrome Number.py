class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0): return False
        temp = x
        result = 0
        while(x != 0):
            y = x % 10
            result = y + result * 10
            x = x/10
        print(result)
        if (result == temp): return True
        else: return False

sol = Solution()
print(sol.isPalindrome(101))
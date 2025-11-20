class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: in
        :rtype: bool
        """
        """ Convert the integer to string and check if it reads the same forwards and backwards. """
        str_x = str(x)
        if str_x != str_x[::-1]:
            return False
        return True
    
# Example usage:
sol = Solution()
print(sol.isPalindrome(121))  # True
print(sol.isPalindrome(-121))  # False
print(sol.isPalindrome(10))  # False
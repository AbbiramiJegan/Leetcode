class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True

x = 121
solution = Solution()
print(solution.isPalindrome(x))

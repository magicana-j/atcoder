class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s_reversed = "".join(list(reversed(s)))
        return s == s_reversed


a = Solution()
print(a.isPalindrome(10))

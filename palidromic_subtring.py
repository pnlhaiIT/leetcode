class Solution:
    def expand(self, s:str, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = self.expand(s, i, i)
            s2 = self.expand(s, i, i+1)
            res = max(res, s1, s2, key=len)
        return res
'''
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
'''
s = "cbbd"
print(Solution().longestPalindrome(s))
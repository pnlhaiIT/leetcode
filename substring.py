class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        cd = 0
        left = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            cd = max(cd, right-left+1)
        return cd

'''
Input: s = "abcabcbb"
Output: 3
'''
s = "abcabcbb"      
print(Solution().lengthOfLongestSubstring(s))
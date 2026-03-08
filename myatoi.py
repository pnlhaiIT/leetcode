class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        result = ""
        sign = 1
        if s == "":
            return 0
        if s[0].isdigit():
            pass
        elif s[0] in ["+","-"]:
            sign = -1 if s[0] == "-" else 1
            s = s[1:]
        else:
            return 0

        for i in range(len(s)):
            if not s[i].isdigit():
                break
            result += s[i]
        if result == "":
            return 0
        result = int(result) * sign
        if result < -2**31:
            return -2**31
        elif result > 2**31-1:
            return 2**31-1
        else:
            return result
'''
Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
'''
s = ' -042'
print(Solution().myAtoi(s))
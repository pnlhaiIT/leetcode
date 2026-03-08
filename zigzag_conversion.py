class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows
        step = 1
        pos = 0
        if numRows == 1:
            return s
        
        for ch in s:
            rows[pos] += ch
            if pos == 0:
                step = 1
            elif pos == numRows-1:
                step = -1
            pos += step

        return "".join(rows)
'''
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I 
'''
s = "PAYPALISHIRING"
numRows = 4
# "PINALSIGYAHRPI"
print(Solution().convert(s,numRows))
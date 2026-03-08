# tự chế thêm zic zac ngang
class Solution:
    def convert(self, s:str, numCol:int) -> str:
        pos = 0
        step = 1
        cols = [""] * numCol
        if numCol == 1:
            return s 
        
        for ch in s:
            cols[pos] += ch
            if pos == 0:
                step = 1
            elif pos == numCol-1:
                step = -1
            pos += step

        return "".join(cols)

s = input("Nhập chuỗi: ").strip()
s = s.replace(" ","")
print(Solution().convert(s,4))   
'''
input: "PHAM NGUYEN LONG HAI", num=4
output: "PUNHGYOGANELHIMNA"
'''    
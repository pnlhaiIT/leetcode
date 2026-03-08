class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        temp = 1
        if x < 0:
            temp = -1
            x *= -1
        elif x == 0:
            return 0

        while x != 0:
            result = result * 10 + x % 10
            x //= 10  
        result *= temp
        if result < -2**31 or result > 2**31-1:
            return 0 
        else:
            return result

x = int(input("Nhập số: "))
print(Solution().reverse(x))
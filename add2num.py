from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        current = temp
        nho = 0

        while l1 or l2 or nho:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            tong = val1 + val2 + nho
            nho = tong // 10

            current.next = ListNode(tong%10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return temp.next

# hàm để test
# hàm tạo dslk từ mảng
def build_list(arr):
    dummy = ListNode()
    current = dummy
    
    for num in arr:
        current.next = ListNode(num)
        current = current.next
        
    return dummy.next
# hàm in mảng từ dslk
def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
# ############
l1 = [2,4,3] 
l2 = [5,6,4]
# output: [7,0,8]
# tạo list
l1 = build_list([2,4,3])
l2 = build_list([5,6,4])

# gọi hàm
sol = Solution()
result = sol.addTwoNumbers(l1, l2)

print(print_list(result))
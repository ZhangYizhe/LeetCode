from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        arr = []

        while True:
            n += 1
            arr += [head.val]

            head = head.next
            if head is None:
                break

        l = 0
        r = n - 1
        max = 0

        while (l < r):
            sum = arr[l] + arr[r]
            if max < sum:
                max = sum
            l += 1
            r -= 1

        return max


headArr = [5,4,2,1]
headArr.reverse()

head = ListNode(headArr[0])


for item in headArr[1:]:
    _head = ListNode(item)
    _head.next = head
    head = _head

print(Solution().pairSum(head))
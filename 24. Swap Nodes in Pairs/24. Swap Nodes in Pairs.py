# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head and head.next:
            point = head.next
        else:
            point = head

        temp_l = head
        prev_l = None

        while temp_l:

            if temp_l.next:
                temp_r = temp_l.next

                if temp_r.next and temp_r.next:
                    temp_l.next = temp_r.next
                else:
                    temp_l.next = None
                temp_r.next = temp_l
                if prev_l:
                    prev_l.next = temp_r
                prev_l = temp_l
                temp_l = temp_l.next
            else:
                temp_l = None

        return point


arr = [1, 2, 3, 4, 5]

node_l = ListNode(arr[0])
point = node_l

for i in range(1, len(arr)):
    node_r = ListNode(arr[i])
    point.next = node_r
    point = node_r

point = Solution().swapPairs(node_l)

while point:
    print(point.val)
    point = point.next
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count_num = 0
        temp_head = head

        while temp_head:
            count_num += 1
            temp_head = temp_head.next

        temp_head = head

        for i in range(1, count_num - n):
            temp_head = temp_head.next

        if count_num - n == 0:
            if temp_head.next:
                return temp_head.next
            else:
                return None

        if temp_head.next:
            temp_head.next = temp_head.next.next

        return head
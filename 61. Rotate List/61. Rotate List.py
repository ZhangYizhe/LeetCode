# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        length = self.node_len(head)

        if length == 0:
            return head

        modelValue = k % length

        if modelValue == 0:
            return head

        currentNode = head

        for i in range(1, length - modelValue):
            currentNode = currentNode.next

        currentNextNode = currentNode.next
        currentNode.next = None

        nextNode = currentNextNode
        while nextNode.next:
            nextNode = nextNode.next

        nextNode.next = head

        return currentNextNode

    def node_len(self, head) -> int:
        _head = head
        res = 0

        while _head:
            res += 1
            _head = _head.next
        return res






head = [1, 2, 3, 4, 5]
k = 2

first_node = ListNode(head[0])
temp_node = first_node

for i in range(1, len(head)):
    _node = ListNode(head[i])

    temp_node.next = _node
    temp_node = _node

node = Solution().rotateRight(first_node, k)
while node:
    print(node.val)
    node = node.next

# ==========

print("=======")
head = [0,1,2]
k = 100

first_node = ListNode(head[0])
temp_node = first_node

for i in range(1, len(head)):
    _node = ListNode(head[i])

    temp_node.next = _node
    temp_node = _node

node = Solution().rotateRight(first_node, k)
while node:
    print(node.val)
    node = node.next

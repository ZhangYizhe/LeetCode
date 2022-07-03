# 61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

![](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)

```python
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```
Example 2:

![](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

```python
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```
**Result**

```python
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
```



[Details ](https://leetcode.com/submissions/detail/737027374/)

Runtime: 45 ms, faster than 77.97% of Python3 online submissions for Rotate List.

Memory Usage: 13.8 MB, less than 79.10% of Python3 online submissions for Rotate List.


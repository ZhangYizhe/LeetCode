# 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

**Example:**

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

**Result**

```swift
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */
class Solution {
    func mergeTwoLists(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        if l1 == nil {
            return l2
        } else {
            if l2 == nil {
                return l1
            }
        }

        if l1!.val > l2!.val {
            l2?.next = mergeTwoLists(l2?.next, l1)
            return l2
        } else {
            l1?.next = mergeTwoLists(l1?.next, l2)
            return l1
        }
    }
}
```



[Details ](https://leetcode.com/submissions/detail/226676895)

Runtime: 16 ms, faster than 100.00% of Swift online submissions for Merge Two Sorted Lists.

Memory Usage: 18.8 MB, less than 42.86% of Swift online submissions for Merge Two Sorted Lists.
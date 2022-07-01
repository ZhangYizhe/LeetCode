# 1. Two Sum

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```



**Result**

```swift
class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var num1Arr : [Int] = readNode(of: l1, parentList: [])
        var num2Arr : [Int] = readNode(of: l2, parentList: [])
        var sumArr : [Int] = []
        
        if num1Arr.count < num2Arr.count {
            let tempArr = num1Arr
            num1Arr = num2Arr
            num2Arr = tempArr
        }
        
        var tempNum = 0
        for i in 0..<num1Arr.count {
            let num1 = num1Arr[i]
            var sum = 0
            if i >= num2Arr.count {
                sum = num1 + tempNum
            } else {
                let num2 = num2Arr[i]
                sum = num1 + num2 + tempNum
            }
            
            tempNum = 0
            if sum >= 10 {
                tempNum = 1
                sumArr.append(sum % 10)
            } else {
                sumArr.append(sum)
            }
        }
        
        if tempNum > 0 {
            sumArr.append(tempNum)
        }
        
        return writeNode(of: sumArr)
    }
    
    func readNode(of node: ListNode?, parentList: [Int] = []) -> [Int] {
        if node == nil {
            return parentList
        }
        let _node = node!
        var _parentList = parentList
        _parentList.append(_node.val)
        if _node.next != nil {
            _parentList = readNode(of: _node.next, parentList: _parentList)
        }
        return _parentList
    }
    
    func writeNode(of nums: [Int]) -> ListNode? {
        var _nums : [Int] = nums
        if _nums.first == nil {
            return nil
        } else {
            let num = _nums.first!
            _nums.removeFirst()
            return ListNode(num, writeNode(of: _nums))
        }
    }
}
```



[Details ](https://leetcode.com/submissions/detail/440059555/)

Runtime: 80 ms, faster than 5.88% of Swift online submissions for Add Two Numbers.

Memory Usage: 14.1 MB, less than 36.94% of Swift online submissions for Add Two Numbers.
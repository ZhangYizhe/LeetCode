# 66. Plus One

Given a **non-empty** array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

**Example 1:**

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

**Example 2:**

```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```



**Result**

```swift
class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var result = digits
        result[result.count - 1] += 1
        for k in (0...(result.count - 1)).reversed() {
            if result[k] == 10 {
                result[k] = 0
                if k-1 < 0 {
                    result.insert(1, at: 0)
                } else {
                    result[k-1] += 1
                }
            } else {
                break
            }
        }
        return result
    }
}
```



[Details ](https://leetcode.com/submissions/detail/240455253)

运行结果

Runtime: 4 ms, faster than 99.29% of Swift online submissions for Plus One.

Memory Usage: 21.2 MB, less than 5.21% of Swift online submissions for Plus One.
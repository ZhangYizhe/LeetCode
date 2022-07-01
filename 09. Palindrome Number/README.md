# 9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

**Example 1:**

```
Input: 121
Output: true
```

**Example 2:**

```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Follow up:**

Coud you solve it without converting the integer to a string?

**Result**

```swift
class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        var _xString = ""
        for number in x.magnitude.description.reversed() {
            _xString += "\(number)"
        }
        
        return x == (Int(_xString) ?? 0)
    }
}
```



[Details ](https://leetcode.com/submissions/detail/226493699)

Runtime: 92 ms, faster than 14.86% of Swift online submissions for Palindrome Number.

Memory Usage: 19.5 MB, less than 14.28% of Swift online submissions for Palindrome Number.
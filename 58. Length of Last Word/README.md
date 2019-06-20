# 58. Length of Last Word

Given a string *s* consists of upper/lower-case alphabets and empty space characters `' '`, return the length of last word in the string.

If the last word does not exist, return 0.

**Note:** A word is defined as a character sequence consists of non-space characters only.

**Example:**

```
Input: "Hello World"
Output: 5
```

 **Result**

```swift
class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        var sArr = s.split(separator: " ")
        return sArr.last?.count ?? 0
    }
}
```

[Details ](https://leetcode.com/submissions/detail/237301697)

运行结果

Runtime: 16 ms, faster than 42.22% of Swift online submissions for Length of Last Word.

Memory Usage: 20.9 MB, less than 5.61% of Swift online submissions for Length of Last Word.
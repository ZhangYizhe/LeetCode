# 20. Valid Parentheses

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1:**

```
Input: "()"
Output: true
```

**Example 2:**

```
Input: "()[]{}"
Output: true
```

**Example 3:**

```
Input: "(]"
Output: false
```

**Example 4:**

```
Input: "([)]"
Output: false
```

**Example 5:**

```
Input: "{[]}"
Output: true
```

**Result**

```swift
class Solution {
    func isValid(_ s: String) -> Bool {
        var stack : [Character] = []
        
        let sArr = Array(s)
        
        for (k, v) in sArr.enumerated() {
            let result = judeg(v)
            if result.1 {
                stack.append(v)
            } else {
                if stack.last == nil {
                    return false
                }
                if judeg(stack.last!).0 == result.0 {
                    stack.removeLast()
                } else {
                    return false
                }
            }
        }
        return stack.isEmpty
    }
    
    func judeg(_ s: Character) -> (Int, Bool) {
        switch s {
        case "(":
            return (1,true)
        case ")":
            return (1,false)
        case "{":
            return (2,true)
        case "}":
            return (2,false)
        case "[":
            return (3,true)
        case "]":
            return (3,false)
        default:
            return (0,false)
        }
    }
}
```



[Details ](https://leetcode.com/submissions/detail/226502789)

Runtime: 8 ms, faster than 100.00% of Swift online submissions for Valid Parentheses.

Memory Usage: 20.1 MB, less than 6.12% of Swift online submissions for Valid Parentheses.
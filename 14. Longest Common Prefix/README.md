# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

```
Input: ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**

```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Note:**

All given inputs are in lowercase letters `a-z`.

**Result**

```swift
class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        if strs.count <= 1 {
            return strs.first ?? ""
        }
        var index = 0
        var returnStr = ""
        let firStrArr = Array(strs.first ?? "")
        
        repeat {
            for _index in 1..<strs.count {
                
                let newStrArray = Array(strs[_index])
                
                if firStrArr.count - 1 < index || newStrArray.count - 1 < index {
                    return returnStr
                }
                
                if newStrArray[index] != firStrArr[index] {
                    return returnStr
                }
            }
            
            returnStr += String(firStrArr[index])
            index += 1
            
        } while (index < firStrArr.count)
        
        return returnStr
    }
}
```



[Details ](https://leetcode.com/submissions/detail/226501588)

Runtime: 72 ms, faster than 19.55% of Swift online submissions for Longest Common Prefix.

Memory Usage: 20 MB, less than 8.89% of Swift online submissions for Longest Common Prefix.
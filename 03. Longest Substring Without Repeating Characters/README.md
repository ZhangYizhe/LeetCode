# 3. Longest Substring Without Repeating Characters



Given a string `s`, find the length of the **longest substring** without repeating characters.



**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Example 4:**

```
Input: s = ""
Output: 0
```



**Result**

```swift
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        
        let sArr = Array(s)
        
        var lengthSet : Set<Int> = sArr.count > 0 ? [1] : []
        for index in 0..<sArr.count {
            var tempCharactersSet : Set<Character> = [sArr[index]]
            for restIndex in index+1..<sArr.count {
                if tempCharactersSet.contains(sArr[restIndex]) {
                    lengthSet.insert(tempCharactersSet.count)
                    break
                }
                
                tempCharactersSet.insert(sArr[restIndex])
                
                if restIndex == sArr.count - 1 {
                    lengthSet.insert(tempCharactersSet.count)
                }
            }
        }
        
        return lengthSet.max() ?? 0
    }
}
```



[Details ](https://leetcode.com/submissions/detail/440614901/)

运行结果

Runtime: 1092 ms, faster than 5.60% of Swift online submissions for Longest Substring Without Repeating Characters.

Memory Usage: 14.7 MB, less than 72.34% of Swift online submissions for Longest Substring Without Repeating Characters.
# 38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```

`1` is read off as `"one 1"` or `11`.
`11` is read off as `"two 1s"` or `21`.
`21` is read off as `"one 2`, then `one 1"` or `1211`.

Given an integer *n* where 1 ≤ *n* ≤ 30, generate the *n*th term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

**Example 1:**

```
Input: 1
Output: "1"
```

**Example 2:**

```
Input: 4
Output: "1211"
```

**Result**

```swift
class Solution {
    func countAndSay(_ n: Int) -> String {
        var tamp = "1"
        if n == 1 {
            return tamp
        }
        for i in 2...n {
            let _tamp = Array(tamp)
            var count = 1
            tamp = ""
            for (key, char) in _tamp.enumerated() {
                if key + 1 > _tamp.count - 1 {
                    tamp += "\(count)\(char)"
                    break
                }
                
                if char == _tamp[key+1] {
                    count += 1
                } else {
                    tamp += "\(count)\(char)"
                    count = 1
                }
                
            }
        }
        
        return tamp
    }
}
```

[Details ](https://leetcode.com/submissions/detail/228335911)

运行结果

Runtime: 12 ms, faster than 92.96% of Swift online submissions for Count and Say.

Memory Usage: 20.9 MB, less than 33.33% of Swift online submissions for Count and Say.
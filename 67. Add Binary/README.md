# 67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both **non-empty** and contains only characters `1` or `0`.

**Example 1:**

```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**

```
Input: a = "1010", b = "1011"
Output: "10101"
```

**Result**

```swift
class Solution {
    func addBinary(_ a: String, _ b: String) -> String {
        
        var aArr = Array(a)
        var bArr = Array(b)
        
        if aArr.count < bArr.count {
            let temp = aArr
            aArr = bArr
            bArr = temp
        }
        
        var aArrCount = aArr.count
        let bArrCount = bArr.count
        
        for k in (0..<bArrCount).reversed() {
            aArrCount = aArr.count
            if bArr[k] == "0" {continue}
            calculation(&aArr, index: (k + (aArrCount - bArrCount)))
        }
        
        return String(aArr)
    }
    
    func calculation(_ arr: inout [Character], index : Int) {
        if arr[index] == "0" {
            arr[index] = "1"
        } else {
            arr[index] = "0"
            
            if index - 1 < 0 {
                arr.insert("1", at: 0)
                return
            }
            if arr[index - 1] == "1" {
                calculation(&arr, index: index - 1)
            } else {
                arr[index-1] = "1"
            }
        }
    }
}
```



[Details ](https://leetcode.com/submissions/detail/240463567)

运行结果

Runtime: 12 ms, faster than 97.92% of Swift online submissions for Add Binary.

Memory Usage: 20.9 MB, less than 5.79% of Swift online submissions for Add Binary.
# 6. ZigZag Conversion

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

 

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

**Example 3:**

```
Input: s = "A", numRows = 1
Output: "A"
```

 

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
- `1 <= numRows <= 1000`

**Result**

```swift
class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        let _s = Array(s)
        
        var _tempIndex = 0
        let _centerNumCount = numRows > 2 ? numRows - 2 : 0
        
        var resultArr : [[String]] = []
        var xIndex = -1
        
        for i in 0..<_s.count {
            let c = String(_s[i])
            
            var sonIndex = numRows - _tempIndex % (numRows + _centerNumCount)
            if sonIndex <= 0 {
                xIndex += 1
                sonIndex = abs(sonIndex)
                resultArr.append([])
                
                if _centerNumCount > 0 {
                    for _ in 1..<(1 + _centerNumCount - sonIndex) {
                        resultArr[xIndex].append("")
                    }
                    resultArr[xIndex].append(c)
                    for _ in resultArr[xIndex].count..<numRows {
                        resultArr[xIndex].append("")
                    }
                } else {
                    resultArr[xIndex].append(c)
                }
                
                if sonIndex == _centerNumCount - 1 {
                    xIndex += 1
                    resultArr.append([])
                }
            } else {
                if sonIndex == numRows {
                    resultArr.append([])
                    xIndex += 1
                }
                resultArr[xIndex].append(c)
            }
            
            _tempIndex += 1
        }
        
        let lastCount = resultArr[resultArr.count-1].count
        for _ in lastCount..<numRows {
            resultArr[resultArr.count-1].append("")
        }

        var resultStrArr = [String](repeating: "", count: numRows)
        for sonArr in resultArr {
            for i in 0..<sonArr.count {
                resultStrArr[i] += sonArr[i]
            }
        }
        
        var resultStr = ""
        for s in resultStrArr {
            resultStr += s
        }
        
        return resultStr
    }
}
```



[Details ](https://leetcode.com/submissions/detail/441990363/)

运行结果

Runtime: 336 ms, faster than 29.12% of Swift online submissions for ZigZag Conversion.

Memory Usage: 19.6 MB, less than 5.49% of Swift online submissions for ZigZag Conversion.
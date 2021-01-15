# 12. Integer to Roman

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

 

**Example 1:**

```
Input: num = 3
Output: "III"
```

**Example 2:**

```
Input: num = 4
Output: "IV"
```

**Example 3:**

```
Input: num = 9
Output: "IX"
```

**Example 4:**

```
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

**Example 5:**

```
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

 

**Constraints:**

- `1 <= num <= 3999`

**Result**

```swift
class Solution {
    func intToRoman(_ num: Int) -> String {
        let numArr = splitNum(by: num)
        var result : String = ""
        numArr.map { num in
            result += numToRomanSpecial(by: num)
        }
        return result
    }
    
    private func splitNum(by num: Int) -> [Int] {
        var result = [Int]()
        let numCharacterArr = Array(String(num))
        let count = numCharacterArr.count
        
        for i in 0..<numCharacterArr.count {
            let num = (Int(String(numCharacterArr[i]))  ?? 0) * Int(pow(10.0, Double(count - i - 1)))
            result.append(num)
        }
        
        return result
    }
    
    private func numToRomanSpecial(by num: Int) -> String {
        
        if num == 0 {
            return ""
        }
        
        var result = ""
        if num < 4 {
            result = "I"
            for _ in 1..<num {
                result += "I"
            }
        } else if num == 4 {
            result = "IV"
        } else if num < 9 {
            result = "V"
            for _ in 5..<num {
                result += "I"
            }
        } else if num == 9 {
            result = "IX"
        } else if num < 40 {
            result = "X"
            for _ in 1..<num / 10 {
                result += "X"
            }
        } else if num == 40 {
            result = "XL"
        } else if num < 90 {
            result = "L"
            for _ in 5..<num / 10 {
                result += "X"
            }
        } else if num == 90 {
            result = "XC"
        } else if num < 400 {
            result = "C"
            for _ in 1..<num / 100 {
                result += "C"
            }
        } else if num == 400 {
            result = "CD"
        } else if num < 900 {
            result = "D"
            for _ in 5..<num / 100 {
                result += "C"
            }
        } else if num == 900 {
            result = "CM"
        } else {
            result = "M"
            for _ in 1..<num / 1000 {
                result += "M"
            }
        }
        
        return result
    }
}
```

[Details ](https://leetcode.com/submissions/detail/443261193/)

运行结果

Runtime: 32 ms, faster than 36.94% of Swift online submissions for Integer to Roman.

Memory Usage: 14.3 MB, less than 22.22% of Swift online submissions for Integer to Roman.
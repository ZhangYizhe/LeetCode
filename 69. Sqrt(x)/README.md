# 69. Sqrt(x)

Implement `int sqrt(int x)`.

Compute and return the square root of *x*, where *x* is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

**Example 1:**

```
Input: 4
Output: 2
```

**Example 2:**

```
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
```

**Result**

```swift
import UIKit

// 牛顿开方法
class Solution {
    func mySqrt(_ x: Int) -> Int {
        var xn = 1.0
        for _ in 0...50 {
            var newX = nextX(xn, a: Double(x))
            if newX == xn { break }
            xn = newX
        }
        return Int(xn)
    }
    
    func nextX(_ x: Double, a: Double) -> Double {
        if x == 0 { return 1 }
        return 0.5 * (x + a / x)
    }
}

print(Solution().mySqrt(4))
```



[Details ](https://leetcode.com/submissions/detail/240903846)

运行结果

Runtime: 8 ms, faster than 91.83% of Swift online submissions for Sqrt(x).

Memory Usage: 20.4 MB, less than 5.66% of Swift online submissions for Sqrt(x).
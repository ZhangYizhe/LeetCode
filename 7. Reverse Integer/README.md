# 7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**

```
Input: 123
Output: 321
```

**Example 2:**

```
Input: -123
Output: -321
```

**Example 3:**

```
Input: 120
Output: 21
```

**Note:**
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

**Result**

```swift
class Solution {
    func reverse(_ x: Int) -> Int {
        let signed = x.signum()
        var _xString = ""
        for number in x.magnitude.description.reversed() {
            _xString += "\(number)"
        }

	    let _x = (Int(_xString) ?? 0) * signed

	    let range = (-1<<31)..<((1<<31) - 1)
	
	    if !range.contains(_x) {
		    return 0
	    }
        return _x
    }
}
```



[Details ](https://leetcode.com/submissions/detail/226207539)

Runtime: 12 ms, faster than 66.85% of Swift online submissions forReverse Integer.

Memory Usage: 19 MB, less than 19.61% of Swift online submissions forReverse Integer.


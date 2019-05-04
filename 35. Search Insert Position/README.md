# 35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

**Example 1:**

```
Input: [1,3,5,6], 5
Output: 2
```

**Example 2:**

```
Input: [1,3,5,6], 2
Output: 1
```

**Example 3:**

```
Input: [1,3,5,6], 7
Output: 4
```

**Example 4:**

```
Input: [1,3,5,6], 0
Output: 0
```

**Result**

```swift
class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        for (k,v) in nums.enumerated() {
            if v >= target {
                if k == 0 {
                    return 0
                }
                return k
            }
        }
        return nums.count
    }
}
```



[Details ](https://leetcode.com/submissions/detail/226682034)

Runtime: 32 ms, faster than 100.00% of Swift online submissions for Search Insert Position.

Memory Usage: 19.7 MB, less than 8.33% of Swift online submissions for Search Insert Position.
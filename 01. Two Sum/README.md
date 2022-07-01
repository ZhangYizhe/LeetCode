# 1. Two Sum

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```



**Result**

```swift
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var result : [Int] = [0, 0]
        for (k,v) in nums.enumerated() {
            for i in k+1..<nums.count {
                if target == (v + nums[i]) {
                    result[0] = k
                    result[1] = i
                    break
                }
            }
            if result.last != 0 {
                break
            }
        }
        return result
    }
}
```



[Details ](https://leetcode.com/submissions/detail/220212897/)

Runtime: 368 ms, faster than 38.95% of Swift online submissions for Two Sum.

Memory Usage: 19.2 MB, less than 46.03% of Swift online submissions for Two Sum.
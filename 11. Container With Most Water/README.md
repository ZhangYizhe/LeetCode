# 11. Container With Most Water

Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

**Notice** that you may not slant the container.

 

**Example 1:**

![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

**Example 3:**

```
Input: height = [4,3,2,1,4]
Output: 16
```

**Example 4:**

```
Input: height = [1,2,1]
Output: 2
```

 

**Constraints:**

- `n == height.length`
- `2 <= n <= 3 * 104`
- `0 <= height[i] <= 3 * 104`

**Result**

```swift
class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var left = 0
        var right = height.count - 1
        var maxArea = 0
        
        while left < right {
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            
            if height[left] > height[right] {
                right -= 1
            } else {
                left += 1
            }
        }
        
        return maxArea
    }
}
```



[Details ](https://leetcode.com/submissions/detail/442817074/)

运行结果

Runtime: 144 ms, faster than 79.64% of Swift online submissions for Container With Most Water.

Memory Usage: 14.7 MB, less than 43.57% of Swift online submissions for Container With Most Water.
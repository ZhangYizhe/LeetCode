# 4. Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

**Follow up:** The overall run time complexity should be `O(log (m+n))`.

**Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Example 3:**

```
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
```

**Example 4:**

```
Input: nums1 = [], nums2 = [1]
Output: 1.00000
```

**Example 5:**

```
Input: nums1 = [2], nums2 = []
Output: 2.00000
```

**Constraints:**

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-106 <= nums1[i], nums2[i] <= 106`



**Result**

```swift
class Solution {
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        var totalNums : [Int] = []
        totalNums.append(contentsOf: nums1)
        totalNums.append(contentsOf: nums2)
        totalNums.sort()
        let count = totalNums.count
        var middleIndex = [Int]()
        
        let tempMiddleNum = count / 2
        
        if count % 2 == 0 {
            middleIndex = [tempMiddleNum - 1, tempMiddleNum]
            return (Double(totalNums[middleIndex[0]]) + Double(totalNums[middleIndex[1]])) / 2
        } else {
            middleIndex = [tempMiddleNum]
            return Double(totalNums[middleIndex[0]])
        }
    }
}
```



[Details ](https://leetcode.com/submissions/detail/440622483/)

运行结果

Runtime: 96 ms, faster than 38.79% of Swift online submissions for Median of Two Sorted Arrays.

Memory Usage: 14.3 MB, less than 96.31% of Swift online submissions for Median of Two Sorted Arrays.
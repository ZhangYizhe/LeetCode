import Cocoa

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

let num1 = [1,3]
let num2 : [Int] = [2]

print(Solution().findMedianSortedArrays(num1, num2))

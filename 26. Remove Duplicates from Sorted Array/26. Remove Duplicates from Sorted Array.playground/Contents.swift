import UIKit

class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        var length : Set<Int> = []
        for num in nums {
            length.insert(num)
        }
        nums = Array(length).sorted()
        return length.count
    }
}

var nums = [1,1,2]

print(Solution().removeDuplicates(&nums))
print(nums)

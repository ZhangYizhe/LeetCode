import UIKit

class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        nums.removeAll(where: { $0 == val })
        return nums.count
    }
}


var nums = [1,1,2]

print(Solution().removeElement(&nums, 1))
print(nums)

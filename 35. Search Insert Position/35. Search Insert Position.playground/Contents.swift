import UIKit

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


print(Solution().searchInsert([1,3,5,6], 0))

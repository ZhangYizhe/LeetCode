import UIKit

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

Solution().twoSum([-1,-2,-3,-4,-5], -8)

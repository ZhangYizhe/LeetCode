import UIKit

class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var result = digits
        result[result.count - 1] += 1
        for k in (0...(result.count - 1)).reversed() {
            if result[k] == 10 {
                result[k] = 0
                if k-1 < 0 {
                    result.insert(1, at: 0)
                } else {
                    result[k-1] += 1
                }
            } else {
                break
            }
        }
        return result
    }
}


print(Solution().plusOne([1,2,3]))

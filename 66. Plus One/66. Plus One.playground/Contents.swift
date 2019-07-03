import UIKit

class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var num = 0;
        var result = [Int]()
        for (k, v) in digits.reversed().enumerated() {
            num += v * Int(pow(Double(10), Double(k)))
        }
        
        num = num + 1
        
        for int in String(num) {
            result.append(Int(String(int)) ?? 0)
        }
        
        return result
    }
}


print(Solution().plusOne([1,3,9]))

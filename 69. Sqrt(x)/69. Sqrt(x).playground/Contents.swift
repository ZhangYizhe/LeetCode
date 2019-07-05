import UIKit

// 牛顿开方法
class Solution {
    func mySqrt(_ x: Int) -> Int {
        var xn = 1.0
        for _ in 0...50 {
            var newX = nextX(xn, a: Double(x))
            if newX == xn { break }
            xn = newX
        }
        return Int(xn)
    }
    
    func nextX(_ x: Double, a: Double) -> Double {
        if x == 0 { return 1 }
        return 0.5 * (x + a / x)
    }
}

print(Solution().mySqrt(4))

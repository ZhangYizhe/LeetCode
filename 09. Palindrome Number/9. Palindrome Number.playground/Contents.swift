import UIKit

class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        var _xString = ""
        for number in x.magnitude.description.reversed() {
            _xString += "\(number)"
        }
        
        return x == (Int(_xString) ?? 0)
    }
}

print(Solution().isPalindrome(121))

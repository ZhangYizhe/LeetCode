import UIKit

class Solution {
    func isValid(_ s: String) -> Bool {
        var stack : [Character] = []
        
        let sArr = Array(s)
        
        for (k, v) in sArr.enumerated() {
            let result = judeg(v)
            if result.1 {
                stack.append(v)
            } else {
                if stack.last == nil {
                    return false
                }
                if judeg(stack.last!).0 == result.0 {
                    stack.removeLast()
                } else {
                    return false
                }
            }
        }
        return stack.isEmpty
    }
    
    func judeg(_ s: Character) -> (Int, Bool) {
        switch s {
        case "(":
            return (1,true)
        case ")":
            return (1,false)
        case "{":
            return (2,true)
        case "}":
            return (2,false)
        case "[":
            return (3,true)
        case "]":
            return (3,false)
        default:
            return (0,false)
        }
    }
}


print(Solution().isValid("([)]"))

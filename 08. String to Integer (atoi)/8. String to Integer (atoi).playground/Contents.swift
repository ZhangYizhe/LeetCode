import Cocoa

class Solution {
    func myAtoi(_ s: String) -> Int {
        var _s = s.trimmingCharacters(in: .whitespacesAndNewlines)
        
        var isPositive = true
        
        if _s.first == "-"  {
            _s.removeFirst()
            isPositive = false
        } else if _s.first == "+" {
            _s.removeFirst()
        }
        
        var resultStr : [Character] = []
        
        for c in _s {
            guard let degital : Int = Int(String(c)) else {
                break
            }
            
            if resultStr.count == 0 && degital == 0 {
                continue
            }
            
            resultStr.append(c)
        }
        
        if resultStr.count == 0 {
            return 0
        }
        
        var result = (Int(String(resultStr)) ?? ((isPositive ? 2147483647 : 2147483648))) * (isPositive ? 1 : -1)
        if result > 2147483647 {
            result = 2147483647
        } else if result < -2147483648 {
            result = -2147483648
        }
        
        return result
    }
}

let s = "words and 987"

print(Solution().myAtoi(s))

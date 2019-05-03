import UIKit

class Solution {
    func romanToInt(_ s: String) -> Int {
        let sArr  = Array(s)
        var sum = 0
        var k = 0
        
        repeat {
            let vInt = self._romanSToInt(String(sArr[k]))
            if sArr.count <= k+1 {
                sum += vInt
                return sum
            }
            let vNextInt = self._romanSToInt(String(sArr[k+1]))
            
            if vInt >= vNextInt {
                sum += vInt
            } else {
                sum += (vNextInt - vInt)
                k += 1
            }
            k += 1
        } while (k < sArr.count)
        return sum
    }
    
    func _romanSToInt(_ s: String) -> Int {
        switch s {
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500
        case "M":
            return 1000
        default:
            return 0
        }
    }
}

print(Solution().romanToInt("MCMXCIV"))

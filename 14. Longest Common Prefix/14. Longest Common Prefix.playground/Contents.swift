import UIKit

class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        if strs.count <= 1 {
            return strs.first ?? ""
        }
        var index = 0
        var returnStr = ""
        let firStrArr = Array(strs.first ?? "")
        
        repeat {
            for _index in 1..<strs.count {
                
                let newStrArray = Array(strs[_index])
                
                if firStrArr.count - 1 < index || newStrArray.count - 1 < index {
                    return returnStr
                }
                
                if newStrArray[index] != firStrArr[index] {
                    return returnStr
                }
            }
            
            returnStr += String(firStrArr[index])
            index += 1
            
        } while (index < firStrArr.count)
        
        return returnStr
    }
}

print(Solution().longestCommonPrefix(["a"]))

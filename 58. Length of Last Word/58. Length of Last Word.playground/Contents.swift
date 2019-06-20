import Cocoa

class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        let sArr = s.split(separator: " ")
        return sArr.last?.count ?? 0
    }
}

var s = " hello world"
print(Solution().lengthOfLastWord(s))

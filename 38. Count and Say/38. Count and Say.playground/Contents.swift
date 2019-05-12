import Cocoa

class Solution {
    func countAndSay(_ n: Int) -> String {
        var tamp = "1"
        if n == 1 {
            return tamp
        }
        for i in 2...n {
            let _tamp = Array(tamp)
            var count = 1
            tamp = ""
            for (key, char) in _tamp.enumerated() {
                if key + 1 > _tamp.count - 1 {
                    tamp += "\(count)\(char)"
                    break
                }
                
                if char == _tamp[key+1] {
                    count += 1
                } else {
                    tamp += "\(count)\(char)"
                    count = 1
                }
                
            }
        }
        
        return tamp
    }
}


print(Solution().countAndSay(10))

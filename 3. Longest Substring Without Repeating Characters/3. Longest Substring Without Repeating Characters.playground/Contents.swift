import Cocoa

class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        
        let sArr = Array(s)
        
        var lengthSet : Set<Int> = sArr.count > 0 ? [1] : []
        for index in 0..<sArr.count {
            var tempCharactersSet : Set<Character> = [sArr[index]]
            for restIndex in index+1..<sArr.count {
                if tempCharactersSet.contains(sArr[restIndex]) {
                    lengthSet.insert(tempCharactersSet.count)
                    break
                }
                
                tempCharactersSet.insert(sArr[restIndex])
                
                if restIndex == sArr.count - 1 {
                    lengthSet.insert(tempCharactersSet.count)
                }
            }
        }
        
        return lengthSet.max() ?? 0
    }
}

let s : String = " "
print(Solution().lengthOfLongestSubstring(s))

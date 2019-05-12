import UIKit

class Solution {
    
    // 尾端逼近
    func strStr(_ haystack: String, _ needle: String) -> Int {
        let _haystack =  Array(haystack)
        let _needle = Array(needle)
        for i in 0...haystack.count {
            for j in (-1..<needle.count).reversed() {
                if j == -1 {return i}
                if i + j >= haystack.count {return -1}
                if _haystack[i + j] != _needle[j] {
                    break
                }
            }
        }
        return -1
    }
    
    // 正向逼近
    func strStr2(_ haystack: String, _ needle: String) -> Int {

        if haystack == needle || needle.isEmpty {
            return 0
        }

        if haystack.isEmpty {
            return -1
        }

        var index = 0
        var _haystack = Array(haystack)

        repeat {
            if _haystack.count - index < needle.count {
                return -1
            }
            if _haystack[index] == needle.first! {
                var _key = 0
                for (key, char) in needle.enumerated() {
                    _key = key
                    if index + _key < haystack.count { // 超过最大
                        if char != _haystack[index + _key] { // 不相符
                            _key -= 1
                            break
                        }
                    } else {
                        return -1
                    }
                }

                if _key == needle.count - 1 {
                    return index
                }
            }

            index += 1

        } while (index < haystack.count)

        return -1
    }
}

print(Solution().strStr("hello", "ll"))

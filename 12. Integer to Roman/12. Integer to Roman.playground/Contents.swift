import Cocoa

class Solution {
    func intToRoman(_ num: Int) -> String {
        let numArr = splitNum(by: num)
        var result : String = ""
        numArr.map { num in
            result += numToRomanSpecial(by: num)
        }
        return result
    }
    
    private func splitNum(by num: Int) -> [Int] {
        var result = [Int]()
        let numCharacterArr = Array(String(num))
        let count = numCharacterArr.count
        
        for i in 0..<numCharacterArr.count {
            let num = (Int(String(numCharacterArr[i]))  ?? 0) * Int(pow(10.0, Double(count - i - 1)))
            result.append(num)
        }
        
        return result
    }
    
    private func numToRomanSpecial(by num: Int) -> String {
        
        if num == 0 {
            return ""
        }
        
        var result = ""
        if num < 4 {
            result = "I"
            for _ in 1..<num {
                result += "I"
            }
        } else if num == 4 {
            result = "IV"
        } else if num < 9 {
            result = "V"
            for _ in 5..<num {
                result += "I"
            }
        } else if num == 9 {
            result = "IX"
        } else if num < 40 {
            result = "X"
            for _ in 1..<num / 10 {
                result += "X"
            }
        } else if num == 40 {
            result = "XL"
        } else if num < 90 {
            result = "L"
            for _ in 5..<num / 10 {
                result += "X"
            }
        } else if num == 90 {
            result = "XC"
        } else if num < 400 {
            result = "C"
            for _ in 1..<num / 100 {
                result += "C"
            }
        } else if num == 400 {
            result = "CD"
        } else if num < 900 {
            result = "D"
            for _ in 5..<num / 100 {
                result += "C"
            }
        } else if num == 900 {
            result = "CM"
        } else {
            result = "M"
            for _ in 1..<num / 1000 {
                result += "M"
            }
        }
        
        return result
    }
}

let num = 10

print(Solution().intToRoman(num))

//Symbol       Value
//I             1
//V             5
//X             10
//L             50
//C             100
//D             500
//M             1000

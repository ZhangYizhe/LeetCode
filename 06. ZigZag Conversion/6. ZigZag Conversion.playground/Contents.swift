import Cocoa

class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        let _s = Array(s)
        
        var _tempIndex = 0
        let _centerNumCount = numRows > 2 ? numRows - 2 : 0
        
        var resultArr : [[String]] = []
        var xIndex = -1
        
        for i in 0..<_s.count {
            let c = String(_s[i])
            
            var sonIndex = numRows - _tempIndex % (numRows + _centerNumCount)
            if sonIndex <= 0 {
                xIndex += 1
                sonIndex = abs(sonIndex)
                resultArr.append([])
                
                if _centerNumCount > 0 {
                    for _ in 1..<(1 + _centerNumCount - sonIndex) {
                        resultArr[xIndex].append("")
                    }
                    resultArr[xIndex].append(c)
                    for _ in resultArr[xIndex].count..<numRows {
                        resultArr[xIndex].append("")
                    }
                } else {
                    resultArr[xIndex].append(c)
                }
                
                if sonIndex == _centerNumCount - 1 {
                    xIndex += 1
                    resultArr.append([])
                }
            } else {
                if sonIndex == numRows {
                    resultArr.append([])
                    xIndex += 1
                }
                resultArr[xIndex].append(c)
            }
            
            _tempIndex += 1
        }
        
        let lastCount = resultArr[resultArr.count-1].count
        for _ in lastCount..<numRows {
            resultArr[resultArr.count-1].append("")
        }

        var resultStrArr = [String](repeating: "", count: numRows)
        for sonArr in resultArr {
            for i in 0..<sonArr.count {
                resultStrArr[i] += sonArr[i]
            }
        }
        
        var resultStr = ""
        for s in resultStrArr {
            resultStr += s
        }
        
        return resultStr
    }
}

let s = "PAYPALISHIRING"
let numRows = 3

print(Solution().convert(s, numRows))

// 1 2 3 *4 5 6 7 *8

// (index / numRows)

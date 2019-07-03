import UIKit

class Solution {
    func addBinary(_ a: String, _ b: String) -> String {
        
        var aArr = Array(a)
        var bArr = Array(b)
        
        if aArr.count < bArr.count {
            let temp = aArr
            aArr = bArr
            bArr = temp
        }
        
        var aArrCount = aArr.count
        let bArrCount = bArr.count
        
        for k in (0..<bArrCount).reversed() {
            aArrCount = aArr.count
            if bArr[k] == "0" {continue}
            calculation(&aArr, index: (k + (aArrCount - bArrCount)))
        }
        
        return String(aArr)
    }
    
    func calculation(_ arr: inout [Character], index : Int) {
        if arr[index] == "0" {
            arr[index] = "1"
        } else {
            arr[index] = "0"
            
            if index - 1 < 0 {
                arr.insert("1", at: 0)
                return
            }
            if arr[index - 1] == "1" {
                calculation(&arr, index: index - 1)
            } else {
                arr[index-1] = "1"
            }
        }
    }
}


print(Solution().addBinary("1010", "1011"))

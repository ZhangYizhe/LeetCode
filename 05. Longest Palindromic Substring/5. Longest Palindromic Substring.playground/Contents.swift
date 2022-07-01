import Cocoa

class Solution {
    func longestPalindrome(_ s: String) -> String {
        let _s : Array = Array(s)
        
        var allString = [String]()
        
        for i in 0..<_s.count {
            var tempLeft = [Character]()
            tempLeft.append(_s[i])
            
            for ii in i+1..<_s.count {
                
                let _tempLeft : [Character] = tempLeft.count > 1 ? Array(String(tempLeft[0...tempLeft.count - 2])) : tempLeft
                if (ii + _tempLeft.count - 1) < _s.count {
                    if String(_tempLeft.reversed()) == String("\(String(_s[(ii)...(ii + _tempLeft.count - 1)]))") {
                        allString.append(String(tempLeft) + String(_s[(ii)...(ii + _tempLeft.count - 1)]))
                        print(123)
                    }
                } else {
                    break
                }
                
                if (ii + tempLeft.count) <= _s.count {
                    if String(tempLeft.reversed()) == String(_s[(ii)...(ii + tempLeft.count - 1)]) {
                        allString.append(String(tempLeft) + String(_s[(ii)...(ii + tempLeft.count - 1)]))
                        print(123)
                    }
                } else {
                    break
                }
                
                tempLeft.append(_s[ii])
            }
        }
        
        allString.sort {
            $0.count > $1.count
        }
        
        return allString.first ?? String(s.first ?? Character(""))
    }
}


let s : String = "forgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
// abcabcabccbacbacba

print(Solution().longestPalindrome(s))

import Cocoa

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var num1Arr : [Int] = readNode(of: l1, parentList: [])
        var num2Arr : [Int] = readNode(of: l2, parentList: [])
        var sumArr : [Int] = []
        
        if num1Arr.count < num2Arr.count {
            let tempArr = num1Arr
            num1Arr = num2Arr
            num2Arr = tempArr
        }
        
        var tempNum = 0
        for i in 0..<num1Arr.count {
            let num1 = num1Arr[i]
            var sum = 0
            if i >= num2Arr.count {
                sum = num1 + tempNum
            } else {
                let num2 = num2Arr[i]
                sum = num1 + num2 + tempNum
            }
            
            tempNum = 0
            if sum >= 10 {
                tempNum = 1
                sumArr.append(sum % 10)
            } else {
                sumArr.append(sum)
            }
        }
        
        if tempNum > 0 {
            sumArr.append(tempNum)
        }
        
        return writeNode(of: sumArr)
    }
    
    func readNode(of node: ListNode?, parentList: [Int] = []) -> [Int] {
        if node == nil {
            return parentList
        }
        let _node = node!
        var _parentList = parentList
        _parentList.append(_node.val)
        if _node.next != nil {
            _parentList = readNode(of: _node.next, parentList: _parentList)
        }
        return _parentList
    }
    
    func writeNode(of nums: [Int]) -> ListNode? {
        var _nums : [Int] = nums
        if _nums.first == nil {
            return nil
        } else {
            let num = _nums.first!
            _nums.removeFirst()
            return ListNode(num, writeNode(of: _nums))
        }
    }
}

//let l1 = Solution().writeNode(of: [9,9,9,9,9,9,9])
//
//let l2 = Solution().writeNode(of: [9,9,9,9])

let l1 = Solution().writeNode(of: [2,4,3])

let l2 = Solution().writeNode(of: [5,6,4])

print(Solution().readNode(of: Solution().addTwoNumbers(l1, l2)))

import UIKit

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}

class Solution {
    func mergeTwoLists(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        if l1 == nil {
            return l2
        } else {
            if l2 == nil {
                return l1
            }
        }
        
        if l1!.val > l2!.val {
            l2?.next = mergeTwoLists(l2?.next, l1)
            return l2
        } else {
            l1?.next = mergeTwoLists(l1?.next, l2)
            return l1
        }
    }
}

//[-10,-9,-6,-4,1,9,9]
//[-5,-3,0,7,8,8]


var l1 = ListNode(1)
l1.next = ListNode(9)
l1.next?.next = ListNode(9)


var l2 = ListNode(7)
l2.next = ListNode(8)
l2.next?.next = ListNode(8)

l1 = Solution().mergeTwoLists(l1, l2)!


repeat {
    print(l1.val)
    if l1.next != nil {
        l1 = l1.next!
    } else {
        break
    }
} while true


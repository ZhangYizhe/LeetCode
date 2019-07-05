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
    func deleteDuplicates(_ head: ListNode?) -> ListNode? {
        
        if head == nil || head?.next == nil {
            return head
        }
        
        if (head?.val ?? 0) == (head?.next?.val ?? 0) {
            if head?.next?.next == nil {
                head?.next = nil
                return head
            } else {
                head?.next = head?.next?.next
                head?.next = deleteDuplicates(head)?.next
            }
        }
        
        head?.next = deleteDuplicates(head?.next)
        
        return head
    }
}

var listNode: ListNode? = ListNode(1)
listNode?.next = ListNode(1)
listNode?.next?.next = ListNode(2)
listNode?.next?.next?.next = ListNode(3)
listNode?.next?.next?.next?.next = ListNode(3)
listNode?.next?.next?.next?.next?.next = ListNode(3)
listNode = Solution().deleteDuplicates(listNode) ?? nil

while listNode != nil {
    print(listNode?.val ?? "")
    listNode = listNode?.next
}

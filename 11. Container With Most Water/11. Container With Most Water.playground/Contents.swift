import Cocoa

class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var left = 0
        var right = height.count - 1
        var maxArea = 0
        
        while left < right {
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            
            if height[left] > height[right] {
                right -= 1
            } else {
                left += 1
            }
        }
        
        return maxArea
    }
}

let h : [Int] = [1,2,1]

print(Solution().maxArea(h))

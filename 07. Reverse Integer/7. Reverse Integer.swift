class Solution {
    func reverse(_ x: Int) -> Int {
        let signed = x.signum()
        var _xString = ""
        for number in x.magnitude.description.reversed() {
            _xString += "\(number)"
        }

	    let _x = (Int(_xString) ?? 0) * signed

	    let range = (-1<<31)..<((1<<31) - 1)
	
	    if !range.contains(_x) {
		    return 0
	    }
        return _x
    }
}

print(Solution().reverse(1563847412))
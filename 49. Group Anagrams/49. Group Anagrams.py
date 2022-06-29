from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = []
        value = []

        for str in strs:
            _str = ''.join(sorted(str))
            if _str in key:
                value[key.index(_str)].append(str)
            else:
                key.append(_str)
                value.append([str])

        return value

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

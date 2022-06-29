# 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

```python
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```
Example 2:

```python
Input: strs = [""]
Output: [[""]]
```
Example 3:

```python
Input: strs = ["a"]
Output: [["a"]]
```
 

**Result**

```python
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
```



[Details ](https://leetcode.com/submissions/detail/733925329/)

Runtime: 972 ms, faster than 5.01% of Python3 online submissions for Group Anagrams.

Memory Usage: 17.2 MB, less than 80.53% of Python3 online submissions for Group Anagrams.


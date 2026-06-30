# Link: https://leetcode.com/problems/valid-anagram/description/

"""Problem Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


## Solution: Time Complexity: O(nlogn); Space Complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False

        s1=sorted(list(s)); t1=sorted(list(t))
        
        for i in range(len(s1)):
            if (s1[i]!=t1[i]):
                return False
        return True

## Alternate Solution: Time Complexity: O(n); Space Complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        
        counter={}
        for char in s:
            counter[char]=counter.get(char, 0)+1
        
        for char in t:
            if (char not in counter or counter[char]==0):
                return False
            counter[char]-=1
        return True

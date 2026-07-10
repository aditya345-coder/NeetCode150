# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""Problem Description:
Given a string s, find the length of the longest substring without duplicate characters.
"""


## Solution: Time Complexity: O(n); Space Complexity: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_list=[]; max_count=0
        for i in range(len(s)):
            max_list=[s[i]]; count=1
            for j in range(i+1,len(s)):
                if (s[j] in max_list):
                    break
                max_list.append(s[j])
            max_count=max(max_count, len(max_list))
        
        return max_count

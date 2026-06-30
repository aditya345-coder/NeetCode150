# Link: https://leetcode.com/problems/binary-search/description/

"""Problem Description:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


## Solution: Time Complexity: O(logn); Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0; high=len(nums)-1

        while(low<=high):
            mid=(high-low)//2 + low
            if (nums[mid]==target):
                return mid
            elif (nums[mid]<target):
                low=mid+1
            else:
                high=mid-1
        return -1

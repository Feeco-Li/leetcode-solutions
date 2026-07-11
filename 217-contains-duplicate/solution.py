# 217: Contains Duplicate
# Difficulty: Easy
# https://leetcode.com/problems/contains-duplicate/
#
# Given an integer array `nums`, return `true` if any value appears **at least
# twice** in the array, and return `false` if every element is distinct.
# 
#  
# 
# **Example 1:**
# 
# **Input:** nums = [1,2,3,1]
# 
# **Output:** true
# 
# **Explanation:**
# 
# The element 1 occurs at the indices 0 and 3.
# 
# **Example 2:**
# 
# **Input:** nums = [1,2,3,4]
# 
# **Output:** false
# 
# **Explanation:**
# 
# All elements are distinct.
# 
# **Example 3:**
# 
# **Input:** nums = [1,1,1,3,3,4,3,2,4,2]
# 
# **Output:** true
# 
#  
# 
# **Constraints:**
# * `1 <= nums.length <= 10⁵`
# * `-10⁹ <= nums[i] <= 10⁹`
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for i in nums:
            if i not in d :
                d[i]=0
            else:
                d[i]+=1
        
        count = Counter(d)
        return any(v>0 for v in d.values())

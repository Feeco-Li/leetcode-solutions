# 283: Move Zeroes
# Difficulty: Easy
# https://leetcode.com/problems/move-zeroes/
#
# Given an integer array `nums`, move all `0`'s to the end of it while maintaining
# the relative order of the non-zero elements.
#
# **Note** that you must do this in-place without making a copy of the array.
#
#
#
# **Example 1:**
#
# **Input:** nums = [0,1,0,3,12]
# **Output:** [1,3,12,0,0]
#
# **Example 2:**
#
# **Input:** nums = [0]
# **Output:** [0]
#
#
#
# **Constraints:**
# * `1 <= nums.length <= 10⁴`
# * `-2³¹ <= nums[i] <= 2³¹ - 1`
#
#
#
# **Follow up:** Could you minimize the total number of operations done?


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1]
        """
        curr = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[curr] = num
                if i != curr:
                    nums[i] = 0
                curr += 1

# 454: 4Sum II
# Difficulty: Medium
# https://leetcode.com/problems/4sum-ii/
#
# Given four integer arrays `nums1`, `nums2`, `nums3`, and `nums4` all of length
# `n`, return the number of tuples `(i, j, k, l)` such that:
# * `0 <= i, j, k, l < n`
# * `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`
#
#
#
# **Example 1:**
#
# **Input:** nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# **Output:** 2
# **Explanation:**
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) +
#  2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) +
#  0 = 0
#
# **Example 2:**
#
# **Input:** nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# **Output:** 1
#
#
#
# **Constraints:**
# * `n == nums1.length`
# * `n == nums2.length`
# * `n == nums3.length`
# * `n == nums4.length`
# * `1 <= n <= 200`
# * `-2²⁸ <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2²⁸`
from collections import defaultdict


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        d = defaultdict(int)
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                key = num1 + num2
                d[key] += 1

        count = 0
        for k, num3 in enumerate(nums3):
            for l, num4 in enumerate(nums4):
                key = -(num3 + num4)
                count += d[key]
        return count

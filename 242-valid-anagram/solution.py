# 242: Valid Anagram
# Difficulty: Easy
# https://leetcode.com/problems/valid-anagram/
#
# Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and
# `false` otherwise.
#
#
#
# **Example 1:**
#
# **Input:** s = "anagram", t = "nagaram"
#
# **Output:** true
#
# **Example 2:**
#
# **Input:** s = "rat", t = "car"
#
# **Output:** false
#
#
#
# **Constraints:**
# * `1 <= s.length, t.length <= 5 * 10⁴`
# * `s` and `t` consist of lowercase English letters.
#
#
#
# **Follow up:** What if the inputs contain Unicode characters? How would you
# adapt your solution to such a case?
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        td = defaultdict(int)
        for ch in s:
            sd[ch] += 1
        for ch in t:
            td[ch] += 1
        return sd == td  # return Counter(s)==Counter(t)

# 5: Longest Palindromic Substring
# Difficulty: Medium
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Given a string `s`, return *the longest* *palindromic* *substring* in `s`.
#
#
#
# **Example 1:**
#
# **Input:** s = "babad"
# **Output:** "bab"
# **Explanation:** "aba" is also a valid answer.
#
# **Example 2:**
#
# **Input:** s = "cbbd"
# **Output:** "bb"
#
#
#
# **Constraints:**
# * `1 <= s.length <= 1000`
# * `s` consist of only digits and English letters.


class Solution:
    def palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res

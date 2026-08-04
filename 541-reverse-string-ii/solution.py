# 541: Reverse String II
# Difficulty: Easy
# https://leetcode.com/problems/reverse-string-ii/
#
# Given a string `s` and an integer `k`, reverse the first `k` characters for
# every `2k` characters counting from the start of the string.
#
# If there are fewer than `k` characters left, reverse all of them. If there are
# less than `2k` but greater than or equal to `k` characters, then reverse the
# first `k` characters and leave the other as original.
#
#
#
# **Example 1:**
#
# **Input:** s = "abcdefg", k = 2
# **Output:** "bacdfeg"
#
# **Example 2:**
#
# **Input:** s = "abcd", k = 2
# **Output:** "bacd"
#
#
#
# **Constraints:**
# * `1 <= s.length <= 10⁴`
# * `s` consists of only lowercase English letters.
# * `1 <= k <= 10⁴`


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sList = list(s)
        n = len(sList)

        def reverseArr(left: int, right: int) -> List:
            while left <= right:
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1
            return s

        for i in range(0, n, 2 * k):
            right = min(i + k - 1, n - 1)
            reverseArr(i, right)

        return "".join(sList)

# 344: Reverse String
# Difficulty: Easy
# https://leetcode.com/problems/reverse-string/
#
# Write a function that reverses a string. The input string is given as an array
# of characters `s`.
#
# You must do this by modifying the input array [in-place][1] with `O(1)` extra
# memory.
#
#
#
# **Example 1:**
#
# **Input:** s = ["h","e","l","l","o"]
# **Output:** ["o","l","l","e","h"]
#
# **Example 2:**
#
# **Input:** s = ["H","a","n","n","a","h"]
# **Output:** ["h","a","n","n","a","H"]
#
#
#
# **Constraints:**
# * `1 <= s.length <= 10⁵`
# * `s[i]` is a [printable ascii character][2].
#
# [1]: https://en.wikipedia.org/wiki/In-place_algorithm
# [2]: https://en.wikipedia.org/wiki/ASCII#Printable_characters


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first, last = 0, len(s) - 1
        firstChar = ""
        lastChar = ""

        while first < last:
            firstChar = s[first]
            lastChar = s[last]
            s[first] = lastChar
            s[last] = firstChar
            first += 1
            last -= 1

# 9: Palindrome Number
# Difficulty: Easy
# https://leetcode.com/problems/palindrome-number/
#
# Given an integer `x`, return `true`* if *`x`* is a ****palindrome****, and
# *`false`* otherwise*.
# 
#  
# 
# **Example 1:**
# 
# **Input:** x = 121
# **Output:** true
# **Explanation:** 121 reads as 121 from left to right and from right to left.
# 
# **Example 2:**
# 
# **Input:** x = -121
# **Output:** false
# **Explanation:** From left to right, it reads -121. From right to left, it becom
# es 121-. Therefore it is not a palindrome.
# 
# **Example 3:**
# 
# **Input:** x = 10
# **Output:** false
# **Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.
# 
#  
# 
# **Constraints:**
# * `-2³¹ <= x <= 2³¹ - 1`
# 
#  
# 
# **Follow up:** Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = str(x)[::-1]
        new_y = str(x)
        result = True
        for i,item in enumerate(new_x):
            if item==new_y[i]:
                continue
            else:
                result = False
                break
        return result

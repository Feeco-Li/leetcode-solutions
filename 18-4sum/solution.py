# 18: 4Sum
# Difficulty: Medium
# https://leetcode.com/problems/4sum/
#
# Given an array `nums` of `n` integers, return *an array of all the **unique**
# quadruplets* `[nums[a], nums[b], nums[c], nums[d]]` such that:
# * `0 <= a, b, c, d < n`
# * `a`, `b`, `c`, and `d` are **distinct**.
# * `nums[a] + nums[b] + nums[c] + nums[d] == target`
# 
# You may return the answer in **any order**.
# 
#  
# 
# **Example 1:**
# 
# **Input:** nums = [1,0,-1,0,-2,2], target = 0
# **Output:** [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# **Example 2:**
# 
# **Input:** nums = [2,2,2,2,2], target = 8
# **Output:** [[2,2,2,2]]
# 
#  
# 
# **Constraints:**
# * `1 <= nums.length <= 200`
# * `-10⁹ <= nums[i] <= 10⁹`
# * `-10⁹ <= target <= 10⁹`

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        # 元素不足 4 个，无法凑成四元组
        if n < 4:
            return []

        # 1. 先进行升序排序，这是双指针和去重的前提
        nums.sort()
        ans = []

        # 外层第一层循环：确定第一个数 nums[i]
        for i in range(n - 3):
            # 去重：如果当前的数与前一个数相同，跳过以防止生成重复四元组
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # --- 剪枝优化 1 ---
            # 当前能拿到的最小四数之和如果都大于 target，后面更大，直接 break 终止
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 当前 nums[i] 加上能拿到的最大三个数如果都小于 target，说明 nums[i] 太小，continue 看下一个
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            # 外层第二层循环：确定第二个数 nums[j]
            for j in range(i + 1, n - 2):
                # 去重：如果当前的数与前一个数相同，跳过（注意起始位置是 i + 1）
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # --- 剪枝优化 2 ---
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                # 2. 内层使用双指针：搜寻后两个数 nums[left] 和 nums[right]
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        # 双指针去重：找到正确答案后，跳过相邻重复的元素
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # 指针收缩
                        left += 1
                        right -= 1

                    elif total < target:
                        # 和偏小，左指针右移以增大 sum
                        left += 1
                    else:
                        # 和偏大，右指针左移以减小 sum
                        right -= 1

        return ans
        

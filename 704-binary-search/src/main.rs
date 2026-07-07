// 704: Binary Search
// Difficulty: Easy
// https://leetcode.com/problems/binary-search/
//
// Given an array of integers `nums` which is sorted in ascending order, and an
// integer `target`, write a function to search `target` in `nums`. If `target`
// exists, then return its index. Otherwise, return `-1`.
//
// You must write an algorithm with `O(log n)` runtime complexity.
//
//
//
// **Example 1:**
//
// **Input:** nums = [-1,0,3,5,9,12], target = 9
// **Output:** 4
// **Explanation:** 9 exists in nums and its index is 4
//
// **Example 2:**
//
// **Input:** nums = [-1,0,3,5,9,12], target = 2
// **Output:** -1
// **Explanation:** 2 does not exist in nums so return -1
//
//
//
// **Constraints:**
// * `1 <= nums.length <= 10⁴`
// * `-10⁴ < nums[i], target < 10⁴`
// * All the integers in `nums` are **unique**.
// * `nums` is sorted in ascending order.

struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        // binary_search returns Ok(index) if found, Err(index_where_it_would_fit) if not
        match nums.binary_search(&target) {
            Ok(index) => index as i32,
            Err(_) => -1,
        }
    }
}

fn main() {
    println!("Run with: cargo test");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        // TODO: add test cases
    }
}

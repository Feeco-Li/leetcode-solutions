// 217: Contains Duplicate
// Difficulty: Easy
// https://leetcode.com/problems/contains-duplicate/
//
// Given an integer array `nums`, return `true` if any value appears **at least
// twice** in the array, and return `false` if every element is distinct.
//
//
//
// **Example 1:**
//
// **Input:** nums = [1,2,3,1]
//
// **Output:** true
//
// **Explanation:**
//
// The element 1 occurs at the indices 0 and 3.
//
// **Example 2:**
//
// **Input:** nums = [1,2,3,4]
//
// **Output:** false
//
// **Explanation:**
//
// All elements are distinct.
//
// **Example 3:**
//
// **Input:** nums = [1,1,1,3,3,4,3,2,4,2]
//
// **Output:** true
//
//
//
// **Constraints:**
// * `1 <= nums.length <= 10⁵`
// * `-10⁹ <= nums[i] <= 10⁹`

struct Solution;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut count: std::collections::HashMap<i32, i32> = std::collections::HashMap::new();
        for num in nums {
            *count.entry(num).or_insert(0) += 1;
        }

        count.into_values().any(|c| c > 1)
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

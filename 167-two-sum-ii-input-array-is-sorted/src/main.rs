// 167: Two Sum II - Input Array Is Sorted
// Difficulty: Medium
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
//
// You are given a **1-indexed** array of integers `numbers` that is already
// **sorted in non-decreasing order**.
//
// Find **two** numbers such that they add up to a specific `target` number. Let
// these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1
// < index2 <= numbers.length`.
//
// Return the indices of the two numbers `index1` and `index2` as an integer array
// `[index1, index2]` of length 2.
//
// The tests are generated such that there is **exactly one solution**. You **may
// not** use the same element twice.
//
// Your solution must use only constant extra space.
//
//
//
// **Example 1:**
//
// **Input:** numbers = [2,7,11,15], target = 9
// **Output:** [1,2]
// **Explanation:** The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We
// return [1, 2].
//
// **Example 2:**
//
// **Input:** numbers = [2,3,4], target = 6
// **Output:** [1,3]
// **Explanation:** The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We r
// eturn [1, 3].
//
// **Example 3:**
//
// **Input:** numbers = [-1,0], target = -1
// **Output:** [1,2]
// **Explanation:** The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We
//  return [1, 2].
//
//
//
// **Constraints:**
// * `2 <= numbers.length <= 3 * 10⁴`
// * `-1000 <= numbers[i] <= 1000`
// * `numbers` is sorted in **non-decreasing order**.
// * `-1000 <= target <= 1000`
// * The tests are generated such that there is **exactly one solution**.

struct Solution;

impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut left = 0;
        let mut right = numbers.len() - 1;

        while left <= right {
            if numbers[left] + numbers[right] > target {
                right = right - 1;
            } else if numbers[left] + numbers[right] < target {
                left = left + 1;
            } else {
                return vec![left + 1, right + 1]
                    .into_iter()
                    .map(|x| x as i32)
                    .collect();
            }
        }

        vec![]
    }
}

fn main() {
    println!("Run with: cargo test");
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_solution() {
        // TODO: add test cases
        assert_eq!(Solution::two_sum([2, 7, 11, 15].to_vec(), 9), [1, 2]);
        assert_eq!(Solution::two_sum([2, 3, 4].to_vec(), 6), [1, 3]);
        assert_eq!(Solution::two_sum([-1, 0].to_vec(), -1), [1, 2]);
    }
}

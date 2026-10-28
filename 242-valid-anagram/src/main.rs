// 242: Valid Anagram
// Difficulty: Easy
// https://leetcode.com/problems/valid-anagram/
//
// Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and
// `false` otherwise.
//
//
//
// **Example 1:**
//
// **Input:** s = "anagram", t = "nagaram"
//
// **Output:** true
//
// **Example 2:**
//
// **Input:** s = "rat", t = "car"
//
// **Output:** false
//
//
//
// **Constraints:**
// * `1 <= s.length, t.length <= 5 * 10⁴`
// * `s` and `t` consist of lowercase English letters.
//
//
//
// **Follow up:** What if the inputs contain Unicode characters? How would you
// adapt your solution to such a case?

struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let s_chars = s.chars();
        let mut s_map = std::collections::HashMap::<char, i32>::new();
        for c in s_chars {
            match s_map.get(&c) {
                Some(v) => s_map.insert(c, v + 1),
                None => s_map.insert(c, 0),
            };
        }

        let t_chars = t.chars();
        let mut t_map = std::collections::HashMap::<char, i32>::new();
        for c in t_chars {
            match t_map.get(&c) {
                Some(v) => t_map.insert(c, v + 1),
                None => t_map.insert(c, 0),
            };
        }

        s_map == t_map
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

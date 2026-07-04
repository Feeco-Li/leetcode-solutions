# leetcode-solutions

Personal LeetCode solutions in Rust, scaffolded and submitted with
[leetui](https://github.com/Feeco-Li/leetui).

## Structure

Each problem lives in its own directory, named `<id>-<slug>`, e.g.:

```
1-two-sum/
├── Cargo.toml
└── src/
    └── main.rs
```

`src/main.rs` contains the problem statement as comments, the
`Solution` implementation, and a `#[cfg(test)]` module with the
example test cases.

## Branches

Each problem also gets its own branch, named after its directory
(e.g. `1-two-sum`). `leetui` creates/switches to it automatically and
pushes there when you commit a solution, so a problem's full solving
history stays isolated on its own branch instead of piling onto
`main`.

## Running a solution locally

```bash
cd 1-two-sum
cargo test
```

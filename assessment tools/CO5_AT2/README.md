# Q36 – Subset Sum Problem for Listing All Valid Subsets

## Overview

This project implements the **Subset Sum Problem** using a **Backtracking Algorithm**.

Given a set of integers and a target sum, the program generates **all possible subsets whose elements add up exactly to the target**.

Unlike a traditional subset-sum solution that may stop after finding one solution, this implementation continues exploring the search space to produce every valid subset.

## Objectives

* Generate all subsets whose sum equals a given target.
* Use recursive backtracking to systematically explore possibilities.
* Include and exclude elements through recursive branching.
* Apply pruning to eliminate invalid branches.
* Avoid duplicate subsets.
* Ensure that all valid subsets are generated.

## Input

The program accepts:

* A set/list of integers.
* A target sum.

Example:

```text
Set = [2, 3, 5, 6, 8, 10]
Target = 10
```

## Output

The program produces a list of all valid subsets whose sum equals the target.

For the given example:

```text
[2, 3, 5]
[2, 8]
[10]
```

Each subset has a sum of `10`.

## Algorithm

The algorithm uses recursive backtracking.

At every stage, an element can be included in the current subset. The algorithm then recursively considers the remaining elements.

When the running sum becomes equal to the target, the current subset is stored as a valid solution.

The algorithm continues searching so that all valid subsets are generated.

## Pruning

For positive integers, a branch can be stopped when:

```text
Current Sum > Target
```

Adding more positive values cannot bring the sum back to the target.

The input is sorted before searching, allowing the algorithm to stop the loop when adding the current value would exceed the target.

## Duplicate Handling

The input is sorted, and duplicate values at the same recursion level are skipped.

This prevents identical subsets from being generated multiple times.

## Complexity

Let `N` be the number of input elements.

### Time Complexity

In the worst case, the algorithm may explore all subsets:

```text
O(2^N)
```

Additional time is required to copy each valid subset into the result list.

### Space Complexity

The recursion depth can reach `N`, and the current subset can contain up to `N` elements.

Therefore, auxiliary space is:

```text
O(N)
```

The output storage is separate and depends on the number and size of valid subsets.

## Technologies

* **Language:** Python
* **Algorithm:** Backtracking
* **Optimization:** Pruning

## Repository Structure

```text
CO4_AT2/
│
├── Question_36/
│   ├── Source_Code/
│   │   └── subset_sum_all.py
│   │
│   ├── Report/
│   │   └── Q36_Report.pdf
│   │
│   └── README.md
│
└── README.md
```

## Conclusion

The project demonstrates how backtracking can systematically explore the subset search space and generate all subsets whose sum equals a given target. Pruning reduces unnecessary exploration, while sorting and duplicate handling ensure efficient and non-redundant output.

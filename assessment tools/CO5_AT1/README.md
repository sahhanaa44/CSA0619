# Q36 – Partition into K Equal Sum Subsets

## Overview

This project solves the **Partition into K Equal Sum Subsets** problem using a **Backtracking Algorithm with Pruning**.

Given a set of positive integers and an integer `K`, the program determines whether the elements can be divided into `K` non-empty subsets such that every subset has the same sum.

## Problem

For a given set:

```text
[4, 3, 2, 3, 5, 2, 1]
```

and:

```text
K = 4
```

The total sum is:

```text
20
```

Therefore, each subset must have:

```text
20 / 4 = 5
```

A valid partition is:

```text
[5]
[4, 1]
[3, 2]
[3, 2]
```

Each subset has a sum of `5`.

## Objectives

* Determine whether an equal-sum partition exists.
* Generate `K` valid subsets.
* Implement recursive backtracking.
* Apply pruning to reduce unnecessary searches.
* Analyze feasibility constraints.
* Prove algorithm correctness.
* Analyze time and space complexity.

## Algorithm

The program uses **Backtracking**.

Each element is assigned to one of the `K` subsets. If adding an element causes a subset to exceed the target sum, that choice is immediately rejected.

The elements are sorted in descending order so that larger values are processed first.

## Pruning Techniques

The implementation uses:

1. **Target Overflow Pruning**
   A number is not added if the subset sum would exceed the target.

2. **Duplicate State Pruning**
   Equivalent subset states are skipped.

3. **Empty Subset Pruning**
   Once an attempt with an empty subset fails, equivalent empty-subset attempts are avoided.

4. **Descending Order**
   Larger elements are considered first, allowing invalid branches to be eliminated earlier.

## Feasibility Conditions

A valid partition is possible only if:

* `K > 0`
* `K <= N`
* The total sum is divisible by `K`.
* No element is greater than the target sum.
* Every element belongs to exactly one subset.
* Every subset is non-empty.
* Every subset has exactly the target sum.

## Complexity

### Time Complexity

Worst-case:

```text
O(K^N)
```

where `N` is the number of elements and `K` is the number of subsets.

Sorting requires `O(N log N)`, but the exponential backtracking dominates.

### Space Complexity

```text
O(N + K)
```

This includes the subsets, subset sums, and recursion stack.

## Input

The program currently uses:

```text
Set = [4, 3, 2, 3, 5, 2, 1]
K = 4
```

## Output

The program displays:

* Total sum
* Target sum
* Whether partitioning is possible
* Each generated subset
* Sum of every subset
* Final validity result

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
│   │   └── partition_k_equal_sum.py
│   │
│   ├── Report/
│   │   └── Q36_Report.pdf
│   │
│   └── README.md
│
└── README.md
```

## Conclusion

The program demonstrates how backtracking can solve the K Equal Sum Subsets problem while pruning invalid and duplicate states. Although pruning improves practical performance, the problem has exponential worst-case complexity and becomes difficult for large input sizes.

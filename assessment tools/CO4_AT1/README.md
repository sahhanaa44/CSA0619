# Q36. Unique Paths in Grid

## Problem Statement

A robot is placed at the top-left corner of an `m × n` grid and needs to reach the bottom-right corner. The robot can move only **right** or **down** at each step.

The objective is to determine the total number of unique paths using **Dynamic Programming**.

---

## Objective

To implement an efficient Dynamic Programming solution to calculate the number of unique paths in a grid.

---

## Input Format

```text
m, n = grid dimensions
```

### Sample Input

```text
m = 3
n = 3
```

---

## Expected Output

```text
Paths = 6
```

---

## Algorithm

1. Create a DP table of size `m × n`.
2. Initialize the first row and first column with `1`.
3. For every remaining cell, calculate the number of paths using:

   ```text
   dp[i][j] = dp[i-1][j] + dp[i][j-1]
   ```
4. Continue until the bottom-right cell is reached.
5. Return the value stored at `dp[m-1][n-1]`.

---

## Source Code

```python
def unique_paths(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Initialize first column
    for i in range(m):
        dp[i][0] = 1

    # Initialize first row
    for j in range(n):
        dp[0][j] = 1

    # Calculate paths
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


# Input
m = 3
n = 3

# Calculate result
paths = unique_paths(m, n)

# Display output
print("Grid Dimensions:", m, "x", n)
print("Paths =", paths)
```

---

## Sample Execution

### Input

```text
m = 3
n = 3
```

### Output

```text
Grid Dimensions: 3 x 3
Paths = 6
```

---

## Dynamic Programming Table

For a `3 × 3` grid, the DP table is:

```text
1  1  1
1  2  3
1  3  6
```

The bottom-right cell contains `6`, which represents the total number of unique paths.

---

## Complexity Analysis

| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  | O(m × n) |
| Space Complexity | O(m × n) |

---

## Technologies Used

* **Language:** Python
* **Algorithm:** Dynamic Programming
* **Concept:** Grid Path Counting

---

## How to Run

1. Save the program as:

```text
unique_paths.py
```

2. Open the terminal in the project directory.

3. Run:

```bash
python unique_paths.py
```

---

## Result

The program successfully calculates the total number of unique paths from the top-left corner to the bottom-right corner of the grid using Dynamic Programming.

For a `3 × 3` grid:

```text
Paths = 6
```

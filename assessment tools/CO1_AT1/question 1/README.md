# Design and Analysis of Algorithms (DAA) – Lab Reports

## Overview

This repository contains the implementation and analysis of two Design and Analysis of Algorithms (DAA) laboratory exercises. Each report includes the objective, problem statement, algorithm, pseudocode, implementation, complexity analysis, and conclusion.

The programs are designed to demonstrate fundamental algorithmic concepts through practical implementations and performance analysis.

---

## Repository Structure

```
├── Question_1_Report.docx
├── Question_2_Report.docx
└── README.md
```

---

## Question 1 – Linear Search

### Aim
Implement the Linear Search algorithm in C and analyze its suitability for searching an unsorted retail product list.

### Description
This program stores a list of products and searches for a specified product using the Linear Search algorithm. Since the list is unsorted, each element is examined sequentially until the required product is found or the list ends.

### Features
- Accepts multiple product names as input.
- Searches for a specified product.
- Displays the position of the product if found.
- Handles cases where the product does not exist.

### Algorithm Summary
1. Read the number of products.
2. Store all product names.
3. Read the search key.
4. Compare the key with each product sequentially.
5. Display the product position if found; otherwise display "Product not found."

### Complexity Analysis

| Case | Time Complexity |
|------|-----------------|
| Best | O(1) |
| Average | O(n) |
| Worst | O(n) |

**Space Complexity:** O(1)

### Conclusion
Linear Search is simple, easy to implement, and well suited for small or frequently updated unsorted datasets where maintaining sorted order is impractical.

---

## Question 2 – Convex Hull Debugging

### Aim
Debug the brute-force Convex Hull algorithm to correctly handle collinear boundary points.

### Description
The original implementation incorrectly rejected all collinear points while determining hull edges. The corrected approach accepts valid collinear boundary points and rejects only points lying outside the candidate edge, ensuring accurate Convex Hull construction.

### Features
- Correct orientation calculation.
- Proper handling of collinear boundary points.
- Validation of points lying on candidate hull edges.
- Improved brute-force Convex Hull logic.

### Algorithm Summary
1. Compute the orientation for every point.
2. Accept collinear points that lie on the candidate edge.
3. Reject candidate edges only if points exist on both sides.
4. Verify that collinear points lie within the line segment.
5. Return valid hull edges.

### Complexity Analysis

**Time Complexity:** O(n³)

- Orientation Check: O(1)
- Overall Brute Force Convex Hull: O(n³)

### Conclusion
The corrected algorithm accurately identifies Convex Hull edges while properly handling collinear boundary points without increasing the overall computational complexity.

---

## Technologies Used

- C Programming
- Basic Computational Geometry
- GCC Compiler
- Standard C Libraries

---

## Learning Outcomes

After completing these exercises, the following concepts are demonstrated:

- Implementation of Linear Search.
- Time and space complexity analysis.
- Brute-force algorithm design.
- Computational geometry fundamentals.
- Convex Hull edge validation.
- Debugging and algorithm optimization.

---

## How to Run

### Compile

```bash
gcc filename.c -o program
```

### Execute

**Windows**

```bash
program.exe
```

**Linux/macOS**

```bash
./program
```

---

## References

- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms*, MIT Press.
- Ellis Horowitz, Sartaj Sahni, and Sanguthevar Rajasekaran, *Fundamentals of Computer Algorithms*.
- Design and Analysis of Algorithms Laboratory Manual.

---

## Author

Prepared as part of the **Design and Analysis of Algorithms (DAA) Laboratory** coursework.

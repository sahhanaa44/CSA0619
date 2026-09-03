# 🎯 DAA Mock Interview

## 📌 About

This repository contains my **Design and Analysis of Algorithms (DAA) Mock Interview preparation**.

The purpose of this mock interview is to practice explaining important DAA concepts, algorithms, problem-solving techniques, and complexity analysis in a clear and interview-ready manner.

---

## 🎤 Mock Interview Format

The interview focuses on:

* Conceptual questions
* Algorithm explanations
* Problem-solving
* Time and space complexity
* Algorithmic techniques
* Examples and dry runs
* Follow-up questions

For each question, the goal is to provide an answer that is:

> **Clear → Correct → Concise → Interview-ready**

---

## 📚 Topics Covered

### 1. Algorithm Analysis

* Time Complexity
* Space Complexity
* Big-O
* Big-Ω
* Big-Θ
* Best, Average, and Worst Case

### 2. Divide and Conquer

* Binary Search
* Merge Sort
* Quick Sort
* Recurrence Relations
* Recursion Tree

### 3. Greedy Algorithms

* Activity Selection
* Fractional Knapsack
* Job Sequencing
* Huffman Coding
* Prim's Algorithm
* Kruskal's Algorithm

### 4. Dynamic Programming

* 0/1 Knapsack
* Longest Common Subsequence
* Matrix Chain Multiplication
* Coin Change
* Fibonacci

### 5. Backtracking

* N-Queens Problem
* Subset Sum Problem
* Graph Coloring
* Hamiltonian Cycle

### 6. Graph Algorithms

* BFS
* DFS
* Dijkstra's Algorithm
* Bellman-Ford Algorithm
* Floyd-Warshall Algorithm
* Topological Sorting

### 7. Sorting Algorithms

* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort
* Heap Sort

---

## 🧠 Questions Practiced

### Backtracking

#### Q1. What is the N-Queens Problem?

The N-Queens problem asks us to place `N` queens on an `N × N` chessboard such that no two queens can attack each other.

A queen can attack another queen if they are in the:

* Same row
* Same column
* Same diagonal

Backtracking is used by placing queens one row at a time and checking whether each position is safe.

---

#### Q2. What is the Subset Sum Problem?

The Subset Sum problem asks whether there exists a subset of a given set of numbers whose sum is equal to a specified target.

**Example:**

```text
Set = {2, 3, 7, 8, 10}
Target = 11
```

A valid subset is:

```text
{3, 8}
```

because:

```text
3 + 8 = 11
```

Using backtracking, each element has two choices:

```text
Include the element
        OR
Exclude the element
```

The algorithm recursively explores these possibilities until it finds a subset whose sum equals the target.

**Time Complexity:** `O(2ⁿ)`

**Space Complexity:** `O(n)`

---

## 🎯 Answer Structure

For each interview question, answers are structured using:

```text
1. Definition
2. Basic idea
3. How it works
4. Example
5. Algorithm / approach
6. Time complexity
7. Space complexity
8. Possible follow-up questions
```

---

## 📝 Mock Interview Rules

During the mock interview:

* Answer the question before looking at the explanation.
* Keep answers concise and precise.
* Explain algorithms in your own words.
* Mention complexity whenever relevant.
* Use examples when explaining concepts.
* Be prepared for follow-up questions.
* Correct mistakes and review weak areas.

---

## 📊 Progress Tracker

| Topic               | Status         |
| ------------------- | -------------- |
| Algorithm Analysis  | ⬜              |
| Divide and Conquer  | ⬜              |
| Greedy Algorithms   | ⬜              |
| Dynamic Programming | ⬜              |
| Backtracking        | 🟡 In Progress |
| Graph Algorithms    | ⬜              |
| Sorting Algorithms  | ⬜              |

### Legend

* ⬜ Not Started
* 🟡 In Progress
* 🟢 Completed

---

## 🚀 Goal

The main goal of this mock interview is to develop the ability to **understand, analyze, and explain algorithms confidently**, rather than simply memorizing definitions.

> **Understand the algorithm → Explain the logic → Analyze complexity → Handle follow-up questions.**

---

## 👩‍💻 Prepared By

**Sahana**

**Subject:** Design and Analysis of Algorithms (DAA)

**Purpose:** Academic & Mock Interview Preparation

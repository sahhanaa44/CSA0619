# Q36 – Bellman-Ford vs Floyd's Algorithm

## Overview

This project implements and compares two shortest-path algorithms:

* **Bellman-Ford Algorithm**
* **Floyd-Warshall Algorithm**

The algorithms are applied to the same weighted graph to demonstrate the difference between **single-source shortest paths** and **all-pairs shortest paths**.

The project analyzes their time complexity, space requirements, scalability, and suitability for different shortest-path problems.

## Objectives

* Implement the Bellman-Ford algorithm.
* Implement the Floyd-Warshall algorithm.
* Find shortest paths using both algorithms.
* Compare single-source and all-pairs approaches.
* Analyze time and space complexity.
* Study the effect of negative edge weights.
* Evaluate scalability for different graph sizes.

## Algorithms Used

### Bellman-Ford

Bellman-Ford finds the shortest paths from **one source vertex** to all other vertices.

It repeatedly relaxes every edge and can handle graphs containing negative edge weights.

**Time Complexity:** `O(VE)`

**Space Complexity:** `O(V)`

### Floyd-Warshall

Floyd-Warshall calculates the shortest paths between **every pair of vertices**.

It uses dynamic programming and updates a distance matrix by considering each vertex as an intermediate vertex.

**Time Complexity:** `O(V³)`

**Space Complexity:** `O(V²)`

## Comparison

| Feature                  | Bellman-Ford   | Floyd-Warshall               |
| ------------------------ | -------------- | ---------------------------- |
| Problem Type             | Single-source  | All-pairs                    |
| Negative Edges           | Supported      | Supported                    |
| Negative Cycle Detection | Yes            | Yes                          |
| Time Complexity          | O(VE)          | O(V³)                        |
| Space Complexity         | O(V)           | O(V²)                        |
| Main Data Structure      | Distance array | Distance matrix              |
| Suitable For             | One source     | All source-destination pairs |

## Graph Used

The program uses a weighted directed graph containing positive and negative edge weights.

The same graph is provided to both algorithms so that their results can be compared.

## Expected Output

The program displays:

* Bellman-Ford shortest distances from the selected source.
* Floyd-Warshall all-pairs shortest-distance matrix.
* Execution time of both algorithms.
* Time and space complexity.
* Comparison and analysis.

## Scalability

Bellman-Ford is generally more suitable when shortest paths are required from only one source. Floyd-Warshall is useful when shortest paths between all pairs of vertices are required.

For large graphs, Floyd-Warshall can require considerable memory because it maintains a `V × V` distance matrix.

## Repository Structure

```text
CO4_AT2/
│
├── Question_36/
│   ├── Source_Code/
│   │   └── bellman_ford_vs_floyd.py
│   │
│   ├── Report/
│   │   └── Q36_Report.pdf
│   │
│   └── README.md
│
└── README.md
```

## Conclusion

The project demonstrates that Bellman-Ford and Floyd-Warshall solve different forms of shortest-path problems. Bellman-Ford is appropriate for single-source shortest paths, while Floyd-Warshall is more suitable when shortest paths between all pairs of vertices are required.

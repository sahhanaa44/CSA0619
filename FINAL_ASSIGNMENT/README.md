# GeoAlgoLab – Hybrid Closest Pair Visualizer

## Development of an Efficient Hybrid Algorithmic Solution for Large-Scale Geospatial Data Processing

GeoAlgoLab is a standalone web application developed for the **CSA0619 – Design and Analysis of Algorithms** assignment.

The application demonstrates, visualizes, and compares three algorithms for finding the closest pair of points in a geospatial dataset:

1. Brute Force
2. Divide and Conquer
3. Hybrid Algorithm

The application combines algorithm visualization, complexity analysis, performance comparison, and threshold optimization in a simple browser-based interface.

---

## 1. Project Objective

The objective of this project is to develop an efficient algorithmic solution for processing large-scale coordinate data and identifying the pair of points with the minimum Euclidean distance.

The project compares the traditional **Brute Force** approach with the **Divide-and-Conquer** approach and develops a **Hybrid Algorithm** that switches to Brute Force for small subproblems.

The Hybrid approach aims to reduce recursive overhead while maintaining the scalability of Divide and Conquer.

---

## 2. Main Features

### Dataset Management

* Generate random coordinate datasets.
* Upload coordinate data using CSV files.
* Display the number of points in the dataset.
* Validate and process coordinate values.

### Algorithms

* Brute Force closest-pair algorithm.
* Divide-and-Conquer closest-pair algorithm.
* Hybrid closest-pair algorithm.
* Display the closest pair.
* Display minimum distance.
* Count distance calculations/comparisons.

### Visualization

* Plot coordinate points on a 2D plane.
* Highlight the closest pair.
* Visualize the median division.
* Display the strip/candidate region.
* Visualize the Hybrid algorithm's switching decision.
* Step-by-step algorithm controls.

### Performance Evaluation

* Execution time measurement.
* Distance comparison count.
* Input-size scalability testing.
* Algorithm comparison.
* Threshold optimization.

### Algorithm Theory

The application explains:

* Big-O notation.
* Big-Ω notation.
* Big-Θ notation.
* Master Theorem.
* Divide-and-Conquer recurrence.
* Hybrid algorithm design.
* Threshold selection.

---

## 3. Algorithms Used

### 3.1 Brute Force Algorithm

The Brute Force algorithm checks every possible pair of points to find the minimum distance.

For `n` points, the number of pair comparisons is:

`n(n-1)/2`

### Time Complexity

**Θ(n²)**

### Advantages

* Simple to understand.
* Easy to implement.
* Suitable for small datasets.
* Useful as a correctness reference.

### Disadvantages

* Becomes slow for large datasets.
* Performs a quadratic number of distance calculations.

---

### 3.2 Divide and Conquer Algorithm

The Divide-and-Conquer algorithm works as follows:

1. Sort points according to their x-coordinate.
2. Divide the points around the median x-coordinate.
3. Recursively find the closest pair in the left half.
4. Recursively find the closest pair in the right half.
5. Check points near the dividing line.
6. Return the minimum distance.

### Recurrence

```text
T(n) = 2T(n/2) + O(n)
```

Using the Master Theorem:

```text
a = 2
b = 2
f(n) = O(n)
```

Therefore:

```text
T(n) = Θ(n log n)
```

### Advantages

* Better scalability than Brute Force.
* Suitable for large datasets.
* Demonstrates Divide-and-Conquer principles.

### Disadvantages

* More complicated than Brute Force.
* Recursive overhead can affect small datasets.
* Efficient implementation of the combine step is important.

---

### 3.3 Hybrid Algorithm

The Hybrid algorithm combines Brute Force and Divide and Conquer.

For each subproblem:

```text
IF n <= T
    Use Brute Force
ELSE
    Use Divide and Conquer
```

Where `T` is the experimentally determined threshold.

The purpose of the threshold is to avoid unnecessary recursive overhead when the number of points becomes small.

### Expected Complexity

The Hybrid algorithm maintains approximately:

```text
Θ(n log n)
```

asymptotic behavior for large inputs while potentially providing better practical performance for small subproblems.

---

## 4. Hybrid Threshold Optimization

The threshold should be determined experimentally rather than simply guessed.

Example threshold values:

```text
2, 4, 8, 16, 32
```

For each threshold:

1. Run the Hybrid algorithm.
2. Measure execution time.
3. Record distance calculations.
4. Test multiple input sizes.
5. Compare the results.
6. Select the threshold with the best practical performance.

The selected value can be represented as:

```text
T* = Experimentally Determined Optimal Threshold
```

The optimal threshold can vary depending on:

* Computer hardware.
* Browser.
* JavaScript engine.
* Dataset characteristics.
* Implementation details.

---

## 5. Dataset Format

The application accepts CSV files containing coordinate data.

Recommended format:

```csv
id,x,y
1,639.4268,15.0065
2,275.0293,133.9264
3,736.4712,406.0197
```

### Required Columns

| Column | Description                   |
| ------ | ----------------------------- |
| `id`   | Unique identifier for a point |
| `x`    | X-coordinate                  |
| `y`    | Y-coordinate                  |

A sample dataset containing 100 coordinate points is provided for testing.

---

## 6. How to Run

GeoAlgoLab is implemented as a **single HTML file**.

No React, Node.js, Python server, database, or installation is required.

### Step 1

Download or copy:

```text
GeoAlgoLab_Hybrid_Closest_Pair.html
```

### Step 2

Double-click the HTML file.

It will open directly in a modern web browser.

Recommended browsers:

* Google Chrome
* Microsoft Edge
* Mozilla Firefox

### Step 3

Use the Dataset section.

You can either:

* Generate a dataset, or
* Upload a CSV dataset.

Then select the required algorithm.

---

## 7. Recommended Demonstration Flow

For project demonstration or viva:

### Step 1

Open the application.

### Step 2

Generate a small dataset.

### Step 3

Run **Brute Force**.

Observe:

* Point comparisons.
* Minimum distance.
* Closest pair.

### Step 4

Run **Divide and Conquer**.

Observe:

* Median division.
* Recursive processing.
* Strip checking.
* Closest pair.

### Step 5

Run **Hybrid**.

Observe:

* Threshold decision.
* Brute Force for small subproblems.
* Divide and Conquer for larger subproblems.

### Step 6

Open the Benchmark section.

Compare:

* Execution time.
* Distance calculations.
* Input size.
* Algorithm scalability.

### Step 7

Run threshold optimization.

Test different threshold values and identify the best-performing threshold.

---

## 8. Correctness Validation

The Brute Force algorithm can be treated as the reference implementation.

For the same dataset:

```text
Brute Force Result
        ↓
Compare with Divide and Conquer Result
        ↓
Compare with Hybrid Result
        ↓
Verify Minimum Distance
        ↓
Verify Closest Pair
```

All algorithms should produce the same minimum distance, allowing for normal floating-point precision.

---

## 9. Performance Metrics

### Execution Time

Measures how long each algorithm takes to process the dataset.

### Distance Calculations

Measures the number of point-pair distance calculations performed.

### Scalability

Measures how algorithm performance changes as the input size increases.

### Memory

Memory usage can also be considered when evaluating the algorithms. Browser-based memory measurements may vary depending on the system and browser.

---

## 10. Complexity Comparison

| Algorithm          | Approach                                | Expected Complexity |
| ------------------ | --------------------------------------- | ------------------- |
| Brute Force        | Compare every pair                      | Θ(n²)               |
| Divide and Conquer | Recursive partitioning + strip checking | Θ(n log n)*         |
| Hybrid             | D&C + Brute Force threshold             | Θ(n log n)*         |

`*` The Θ(n log n) bound assumes an efficient implementation of the combine step.

---

## 11. Euclidean Distance

The application uses Euclidean distance:

```text
d = √((x₂ - x₁)² + (y₂ - y₁)²)
```

For two points:

```text
P₁ = (x₁, y₁)
P₂ = (x₂, y₂)
```

the distance is calculated using the above formula.

Squared distance can also be used for performance comparisons:

```text
d² = (x₂ - x₁)² + (y₂ - y₁)²
```

This avoids an unnecessary square-root operation when only distances need to be compared.

---

## 12. Geospatial Data Assumption

For this academic demonstration, coordinates are treated as points in a 2D Cartesian plane.

If actual latitude and longitude coordinates are used in a production GIS system, ordinary Euclidean distance is not generally the correct geographic distance.

A production system should consider:

* Projected coordinate systems, or
* Geodesic distance calculations.

The current project uses Euclidean distance because it is suitable for demonstrating the closest-pair algorithms.

---

## 13. System Requirements

### Hardware

A normal computer or laptop is sufficient.

### Software

A modern web browser is required.

Recommended:

* Google Chrome
* Microsoft Edge
* Mozilla Firefox

### Internet

Internet access is not required after obtaining the HTML file.

The application runs locally in the browser.

---

## 14. Technologies Used

The project uses:

* HTML5
* CSS3
* JavaScript
* HTML Canvas
* Browser Performance API

No external JavaScript framework is required.

---

## 15. Project Methodology

The project follows this methodology:

```text
Dataset
   ↓
Data Preparation
   ↓
Brute Force
   ↓
Divide and Conquer
   ↓
Hybrid Algorithm
   ↓
Threshold Determination
   ↓
Complexity Analysis
   ↓
Experimental Evaluation
   ↓
Performance Comparison
   ↓
Optimization
   ↓
Final Engineering Decision
```

---

## 16. Expected Engineering Decision

The project does not assume that one algorithm is always the best.

Instead:

* Brute Force is appropriate for small datasets.
* Divide and Conquer is more scalable for large datasets.
* Hybridization can improve practical performance by using Brute Force for small subproblems.
* The threshold should be selected using experimental results.

Therefore, the Hybrid algorithm aims to provide a practical balance between:

**Low overhead for small inputs + Scalability for large inputs**

---

## 17. Limitations

This project is an educational browser-based implementation.

Limitations include:

1. Browser execution time can vary between runs.
2. JavaScript performance depends on the computer and browser.
3. Very large datasets may be limited by browser memory.
4. Random coordinates may not represent real-world geographic distributions.
5. Euclidean distance is a simplified model for geographic coordinates.
6. Browser memory measurements may not be directly comparable with native applications.
7. Visualization focuses on understanding the algorithms rather than exposing every internal operation.

---

## 18. Experimental Results

Actual benchmark values should be obtained by running the application.

**Do not use fabricated experimental values.**

Record results in a table such as:

| Input Size | Brute Force Time | D&C Time | Hybrid Time | Best Threshold |
| ---------: | ---------------: | -------: | ----------: | -------------: |
|        100 |         Measured | Measured |    Measured |       Measured |
|        500 |         Measured | Measured |    Measured |       Measured |
|       1000 |         Measured | Measured |    Measured |       Measured |
|       5000 |         Measured | Measured |    Measured |       Measured |

All algorithms should use:

* The same input dataset.
* The same computer.
* The same browser.
* The same experimental conditions.

---

## 19. SDG 9 Relevance

The project is related to **United Nations Sustainable Development Goal 9 – Industry, Innovation and Infrastructure**.

Efficient geospatial algorithms can support:

* Infrastructure planning.
* Facility placement.
* Network planning.
* Location analysis.
* Spatial decision support.
* Large-scale geographic data processing.

Improving algorithm efficiency can help systems process increasing amounts of spatial data more effectively.

---

## 20. Project Files

A complete project package can contain:

```text
GeoAlgoLab/
│
├── GeoAlgoLab_Hybrid_Closest_Pair.html
├── sample_geospatial_points.csv
├── README.md
└── DAA_Hybrid_Closest_Pair_Assignment_Report.docx
```

### File Descriptions

**GeoAlgoLab_Hybrid_Closest_Pair.html**

Main interactive web application.

**sample_geospatial_points.csv**

Sample coordinate dataset for testing the algorithms.

**README.md**

Project documentation and instructions.

**DAA_Hybrid_Closest_Pair_Assignment_Report.docx**

Complete assignment report containing the problem, methodology, algorithms, complexity analysis, evaluation, engineering decision, reflection, and references.

---

## 21. Academic Information

**Course:** CSA0619 – Design and Analysis of Algorithms

**Assignment:** Development of an Efficient Hybrid Algorithmic Solution for Large-Scale Geospatial Data Processing

**Institution:** SIMATS Engineering
Saveetha Institute of Medical and Technical Sciences
Chennai – 602105

**Academic Year:** 2026–2027

**Date:** September 2026

---

## 22. Conclusion

GeoAlgoLab provides an interactive environment for understanding and evaluating closest-pair algorithms for large-scale coordinate data.

The application demonstrates that:

* Brute Force provides a simple baseline.
* Divide and Conquer improves asymptotic scalability.
* Hybridization combines the strengths of both approaches.
* Experimental threshold selection can improve practical performance.
* Visualization makes algorithm behavior easier to understand.
* Benchmarking supports evidence-based engineering decisions.

The overall project connects **algorithm theory, implementation, visualization, experimentation, optimization, and engineering decision-making** in a single simple web application.

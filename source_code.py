def unique_paths(m, n):
    # Create DP table
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # First column
    for i in range(m):
        dp[i][0] = 1

    # First row
    for j in range(n):
        dp[0][j] = 1

    # Fill the remaining cells
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


# Input
m = 3
n = 3

# Calculate unique paths
paths = unique_paths(m, n)

# Output
print("Grid Dimensions:", m, "x", n)
print("Paths =", paths)

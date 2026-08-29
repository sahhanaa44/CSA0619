# Q36 - Bellman-Ford vs Floyd-Warshall Algorithm
# Shortest Path Comparison

INF = float('inf')


# ---------------------------------------------------------
# Bellman-Ford Algorithm
# ---------------------------------------------------------
def bellman_ford(vertices, edges, source):
    distance = [INF] * vertices
    distance[source] = 0

    # Relax all edges V-1 times
    for _ in range(vertices - 1):
        updated = False

        for u, v, weight in edges:
            if distance[u] != INF and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                updated = True

        if not updated:
            break

    # Check for negative weight cycle
    for u, v, weight in edges:
        if distance[u] != INF and distance[u] + weight < distance[v]:
            return None, True

    return distance, False


# ---------------------------------------------------------
# Floyd-Warshall Algorithm
# ---------------------------------------------------------
def floyd_warshall(vertices, edges):
    distance = [[INF] * vertices for _ in range(vertices)]

    # Distance from a vertex to itself is zero
    for i in range(vertices):
        distance[i][i] = 0

    # Initialize edge weights
    for u, v, weight in edges:
        distance[u][v] = weight

    # Dynamic programming
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if distance[i][k] != INF and distance[k][j] != INF:
                    distance[i][j] = min(
                        distance[i][j],
                        distance[i][k] + distance[k][j]
                    )

    # Check for negative cycle
    negative_cycle = False

    for i in range(vertices):
        if distance[i][i] < 0:
            negative_cycle = True
            break

    return distance, negative_cycle


# ---------------------------------------------------------
# Display Bellman-Ford Result
# ---------------------------------------------------------
def display_bellman_ford(distance, source):
    print("\nBELLMAN-FORD RESULT")
    print("-" * 45)
    print(f"Source Vertex: V{source}")

    print(f"\n{'Vertex':<15}{'Shortest Distance':<20}")
    print("-" * 45)

    for i, d in enumerate(distance):
        if d == INF:
            print(f"V{i:<14}{'INF':<20}")
        else:
            print(f"V{i:<14}{d:<20}")


# ---------------------------------------------------------
# Display Floyd-Warshall Result
# ---------------------------------------------------------
def display_floyd(distance):
    print("\nFLOYD-WARSHALL RESULT")
    print("-" * 65)

    print(f"{' ':<8}", end="")

    for i in range(len(distance)):
        print(f"{'V' + str(i):<10}", end="")

    print()
    print("-" * 65)

    for i in range(len(distance)):
        print(f"{'V' + str(i):<8}", end="")

        for j in range(len(distance)):
            if distance[i][j] == INF:
                print(f"{'INF':<10}", end="")
            else:
                print(f"{distance[i][j]:<10}", end="")

        print()


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------

vertices = 5

# Directed weighted graph
# (source, destination, weight)
edges = [
    (0, 1, 6),
    (0, 2, 7),
    (1, 2, 8),
    (1, 3, 5),
    (1, 4, -4),
    (2, 3, -3),
    (2, 4, 9),
    (3, 1, -2),
    (4, 0, 2),
    (4, 3, 7)
]

source = 0

print("=" * 65)
print("        BELLMAN-FORD VS FLOYD-WARSHALL")
print("             SHORTEST PATH ANALYSIS")
print("=" * 65)

print("\nGRAPH INFORMATION")
print("-" * 65)

print("Number of Vertices:", vertices)
print("Number of Edges   :", len(edges))
print("Source Vertex     : V0")

print("\nEdges:")
for u, v, w in edges:
    print(f"V{u} -> V{v}  Weight = {w}")


# Bellman-Ford
bellman_distance, bf_negative_cycle = bellman_ford(
    vertices,
    edges,
    source
)

if bf_negative_cycle:
    print("\nBellman-Ford detected a negative weight cycle.")
else:
    display_bellman_ford(bellman_distance, source)


# Floyd-Warshall
floyd_distance, fw_negative_cycle = floyd_warshall(
    vertices,
    edges
)

if fw_negative_cycle:
    print("\nFloyd-Warshall detected a negative weight cycle.")
else:
    display_floyd(floyd_distance)


# ---------------------------------------------------------
# Comparison
# ---------------------------------------------------------

print("\n" + "=" * 65)
print("                 ALGORITHM COMPARISON")
print("=" * 65)

print("\nBellman-Ford")
print("Purpose          : Single-source shortest paths")
print("Time Complexity  : O(VE)")
print("Space Complexity : O(V)")
print("Negative Edges   : Supported")

print("\nFloyd-Warshall")
print("Purpose          : All-pairs shortest paths")
print("Time Complexity  : O(V^3)")
print("Space Complexity : O(V^2)")
print("Negative Edges   : Supported")

print("\nAnalysis")
print("-" * 65)

print("Bellman-Ford is preferred when shortest paths from")
print("one source vertex are required.")

print("\nFloyd-Warshall is preferred when shortest paths between")
print("every pair of vertices are required.")

print("\nFor large graphs, Bellman-Ford generally uses less")
print("memory, while Floyd-Warshall requires a V x V matrix.")

print("\n" + "=" * 65)
print("                     END OF PROGRAM")
print("=" * 65)

# Q36 - Partition into K Equal Sum Subsets
# Backtracking with Pruning

def can_partition(nums, k):
    total_sum = sum(nums)

    # Constraint 1: Total sum must be divisible by k
    if total_sum % k != 0:
        return False, []

    target = total_sum // k

    # There cannot be more subsets than elements
    if k > len(nums):
        return False, []

    # If any number is greater than target,
    # it cannot belong to any valid subset
    if max(nums) > target:
        return False, []

    # Sort in descending order for better pruning
    nums.sort(reverse=True)

    subsets = [[] for _ in range(k)]
    subset_sums = [0] * k

    def backtrack(index):
        # All elements have been assigned
        if index == len(nums):
            return all(s == target for s in subset_sums)

        current = nums[index]
        previous_sum = -1

        for i in range(k):

            # Pruning 1:
            # Do not try identical subset states
            if subset_sums[i] == previous_sum:
                continue

            # Pruning 2:
            # Do not exceed target sum
            if subset_sums[i] + current > target:
                continue

            previous_sum = subset_sums[i]

            # Add current element
            subsets[i].append(current)
            subset_sums[i] += current

            if backtrack(index + 1):
                return True

            # Backtrack
            subsets[i].pop()
            subset_sums[i] -= current

            # Pruning 3:
            # If an empty subset was tried and failed,
            # there is no need to try other empty subsets
            if subset_sums[i] == 0:
                break

        return False

    if backtrack(0):
        return True, subsets

    return False, []


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------

print("=" * 65)
print("       PARTITION INTO K EQUAL SUM SUBSETS")
print("             BACKTRACKING + PRUNING")
print("=" * 65)

# Sample input
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4

print("\nInput Set:", nums)
print("Number of Subsets (K):", k)

total_sum = sum(nums)
print("Total Sum:", total_sum)

if total_sum % k == 0:
    target = total_sum // k
    print("Target Sum for Each Subset:", target)
else:
    print("Target Sum: Not possible")


possible, subsets = can_partition(nums, k)

print("\n" + "-" * 65)

if possible:
    print("PARTITION POSSIBLE")
    print("-" * 65)

    for i, subset in enumerate(subsets, start=1):
        print(
            f"Subset {i}: {subset}"
            f"    Sum = {sum(subset)}"
        )

    print("-" * 65)
    print("All subsets have equal sum.")
    print("Result: VALID PARTITION")

else:
    print("PARTITION NOT POSSIBLE")
    print("-" * 65)
    print("No valid partition into", k, "equal-sum subsets exists.")

print("=" * 65)

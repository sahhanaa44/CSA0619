# Q36 - Subset Sum Problem for Listing All Valid Subsets
# Backtracking Algorithm

def find_subsets(nums, target):
    valid_subsets = []
    current_subset = []

    def backtrack(index, current_sum):
        # If current sum equals target,
        # store the current subset
        if current_sum == target:
            valid_subsets.append(current_subset.copy())
            return

        # If all elements have been processed
        if index == len(nums):
            return

        # Pruning:
        # For positive integers, a sum greater than
        # the target cannot become a valid solution.
        if current_sum > target:
            return

        # Try including each remaining element
        for i in range(index, len(nums)):

            # Skip duplicate elements at the same level
            if i > index and nums[i] == nums[i - 1]:
                continue

            # Pruning before adding the element
            if current_sum + nums[i] > target:
                break

            # Include the current element
            current_subset.append(nums[i])

            backtrack(i + 1, current_sum + nums[i])

            # Backtrack: remove the element
            current_subset.pop()

    # Sort to make duplicate handling easier
    nums.sort()

    backtrack(0, 0)

    return valid_subsets


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------

print("=" * 65)
print("       SUBSET SUM - ALL VALID SUBSETS")
print("             BACKTRACKING ALGORITHM")
print("=" * 65)

# Input
nums = [2, 3, 5, 6, 8, 10]
target = 10

print("\nInput Set   :", nums)
print("Target Sum  :", target)

# Find all valid subsets
result = find_subsets(nums, target)

# Display result
print("\n" + "-" * 65)
print("VALID SUBSETS")
print("-" * 65)

if result:
    for i, subset in enumerate(result, start=1):
        print(
            f"Subset {i}: {subset}"
            f"    Sum = {sum(subset)}"
        )
else:
    print("No valid subset found.")

print("-" * 65)
print("Total Valid Subsets:", len(result))

print("=" * 65)
print("                     END OF PROGRAM")
print("=" * 65)

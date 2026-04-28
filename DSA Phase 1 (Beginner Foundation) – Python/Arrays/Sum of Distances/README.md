# Sum of Distances (Beginner Approach)

## Problem

For each index, find the sum of distances to all other indices having the same value.

## Approach (Simple)

1. Loop through each index `i`
2. For each `i`, loop through all `j`
3. If values match → add `|i - j|`

## Code

```python
def distance(nums):
    n = len(nums)
    result = [0] * n

    for i in range(n):
        total = 0
        for j in range(n):
            if i != j and nums[i] == nums[j]:
                total += abs(i - j)
        result[i] = total

    return result
```

## Complexity

* Time: O(n²)
* Space: O(n)

## Note

This is a beginner-friendly approach. For large inputs, an optimized solution using prefix sums is required.

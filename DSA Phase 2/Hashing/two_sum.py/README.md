# Two Sum

## Problem

Given an array and a target, find two indices such that their values add up to the target.

## Approach

Use a dictionary to store visited numbers and their indices.

For each number:

* Check if (target - current) exists
* If yes → return indices

## Code

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i
```

## Complexity

* Time: O(n)
* Space: O(n)

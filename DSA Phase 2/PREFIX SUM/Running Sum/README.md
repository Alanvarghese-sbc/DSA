# Running Sum of Array

## Problem

Return the running sum of an array.

## Approach

Keep a cumulative sum and update it while traversing.

## Code

```python
def running_sum(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result
```

## Complexity

* Time: O(n)
* Space: O(n)

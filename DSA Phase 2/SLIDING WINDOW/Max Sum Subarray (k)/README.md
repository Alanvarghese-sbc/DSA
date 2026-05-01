# Maximum Sum Subarray of Size K

## Problem

Find the maximum sum of any subarray of size k.

## Approach

Use sliding window:

* Add next element
* Remove previous element

## Code

```python
def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

## Complexity

* Time: O(n)
* Space: O(1)

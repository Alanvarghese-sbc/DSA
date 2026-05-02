# Subarray Sum Equals K

## Problem

Count number of subarrays whose sum equals k.

## Approach

* Use prefix sum + hashmap
* Check if (prefix_sum - k) exists

## Code

```python
def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    hashmap = {0: 1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in hashmap:
            count += hashmap[prefix_sum - k]

        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

    return count
```

## Complexity

* Time: O(n)
* Space: O(n)

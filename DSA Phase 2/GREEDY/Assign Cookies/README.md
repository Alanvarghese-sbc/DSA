# Assign Cookies

## Problem

Assign cookies to children such that maximum children are satisfied.

## Approach

Sort both arrays and assign smallest possible cookie.

## Code

```python
def find_content_children(g, s):
    g.sort()
    s.sort()

    i = j = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1

    return i
```

## Complexity

* Time: O(n log n)
* Space: O(1)

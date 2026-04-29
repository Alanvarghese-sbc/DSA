# Valid Palindrome

## Problem

Check if a string is a palindrome (ignore non-alphanumeric characters).

## Approach

Use two pointers:

* Compare left and right characters
* Move inward

## Code

```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

## Complexity

* Time: O(n)
* Space: O(n)

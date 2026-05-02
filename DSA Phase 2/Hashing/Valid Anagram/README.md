# Valid Anagram

## Problem

Check if two strings are anagrams.

## Approach

* Count frequency of characters in first string
* Reduce count using second string
* If all counts become zero → valid

## Code

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True
```

## Complexity

* Time: O(n)
* Space: O(n)

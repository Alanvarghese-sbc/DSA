# 📊 Find the Frequency of Each Element (Python)

## 📌 Problem Statement

Given an integer array, print the frequency of every element.

**Note:**
- ❌ Do not use `collections.Counter`
- ✅ Use a Python Dictionary (`dict`)

---

## 📥 Input Format

- First line contains an integer `n` (size of the array).
- Second line contains `n` space-separated integers.

---

## 📤 Output Format

Print each element followed by its frequency.

---

## 🧾 Example

### Input

```text
7
1 2 2 3 1 4 2
```

### Output

```text
1 : 2
2 : 3
3 : 1
4 : 1
```

---

# 🧠 Approach 1: Using `if...else`

### Algorithm

1. Create an empty dictionary.
2. Traverse the array one element at a time.
3. Check whether the element already exists in the dictionary.
   - If it exists, increment its frequency.
   - Otherwise, insert it with a frequency of `1`.
4. Print the dictionary.

---

## 💻 Python Code

```python
n = int(input())
arr = list(map(int, input().split()))

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for key, value in frequency.items():
    print(key, ":", value)
```

---

## 🔍 Dry Run

Array:

```text
[1, 2, 2, 3, 1, 4, 2]
```

| Element | Dictionary |
|---------|------------|
| 1 | {1:1} |
| 2 | {1:1, 2:1} |
| 2 | {1:1, 2:2} |
| 3 | {1:1, 2:2, 3:1} |
| 1 | {1:2, 2:2, 3:1} |
| 4 | {1:2, 2:2, 3:1, 4:1} |
| 2 | {1:2, 2:3, 3:1, 4:1} |

---

# 🧠 Approach 2: Using `dict.get()`

Python dictionaries provide the `get()` method.

Syntax:

```python
dictionary.get(key, default_value)
```

- Returns the value if the key exists.
- Otherwise returns the default value.

---

## 💻 Python Code

```python
n = int(input())
arr = list(map(int, input().split()))

frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

for key, value in frequency.items():
    print(key, ":", value)
```

---

## 🔍 How `get()` Works

Initially:

```python
frequency = {}
```

First element:

```python
frequency[1] = frequency.get(1, 0) + 1
```

Since `1` is not present,

```python
frequency.get(1, 0)
```

returns

```python
0
```

Therefore,

```python
frequency[1] = 0 + 1
```

Dictionary becomes:

```python
{1:1}
```

Next occurrence of `1`:

```python
frequency[1] = frequency.get(1, 0) + 1
```

Now,

```python
frequency.get(1, 0)
```

returns

```python
1
```

So,

```python
frequency[1] = 1 + 1
```

Dictionary becomes:

```python
{1:2}
```

---

# 📚 Dictionary Methods Used

## `items()`

Returns both keys and values.

```python
for key, value in frequency.items():
    print(key, value)
```

Example:

```python
frequency = {
    1:2,
    2:3,
    3:1
}
```

Output:

```text
1 2
2 3
3 1
```

---

## `keys()`

Returns only the keys.

```python
for key in frequency.keys():
    print(key)
```

Output:

```text
1
2
3
```

---

## `values()`

Returns only the values.

```python
for value in frequency.values():
    print(value)
```

Output:

```text
2
3
1
```

---

# ⏱ Time & Space Complexity

| Operation | Complexity |
|-----------|------------|
| Building Dictionary | **O(n)** |
| Printing Frequencies | **O(k)** |
| Overall Time | **O(n)** |
| Space Complexity | **O(k)** |

Where:

- `n` = Total number of elements
- `k` = Number of unique elements

---

# 🔥 Key Concepts

- Dictionary (`dict`)
- Hash Map
- Key-Value Pair
- Frequency Counting
- Dictionary Traversal
- `items()`
- `get()`

---

# ⚠️ Edge Cases

- Empty array
- All elements are the same
- All elements are unique
- Negative numbers
- Large input size

---

# 💡 Interview Tips

- Dictionary lookup is **O(1)** on average.
- Frequency counting is one of the most common interview patterns.
- Learn both approaches:
  - Using `if...else`
  - Using `dict.get()`

The `dict.get()` approach is shorter and more Pythonic, while the `if...else` approach is easier to understand for beginners.

---

# 🚀 Related Problems

- Count Character Frequency
- First Non-Repeating Element
- Most Frequent Element
- Find Duplicates in an Array
- Group Anagrams
- Two Sum

---

## 📌 Author

**Alan Varghese**
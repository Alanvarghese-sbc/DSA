# Check if Array is Sorted

## 📌 Problem Statement

Given an array of integers, determine whether the array is sorted in **non-decreasing order**.

* Print `"Sorted"` if the array is sorted.
* Otherwise, print `"Not Sorted"`.

> **Note:** In a non-decreasing array, duplicate elements are allowed.

---

# Example 1

### Input

```text
5
1 2 3 4 5
```

### Output

```text
Sorted
```

### Explanation

Each element is less than or equal to the next element, so the array is sorted.

---

# Example 2

### Input

```text
5
1 3 2 4 5
```

### Output

```text
Not Sorted
```

### Explanation

The element `3` is greater than `2`, so the array is not sorted.

---

# Example 3

### Input

```text
6
1 2 2 3 5 5
```

### Output

```text
Sorted
```

### Explanation

Duplicate elements are allowed in a non-decreasing sorted array.

---

# 💡 Approach

Traverse the array from left to right and compare every element with its next element.

* If `arr[i] <= arr[i + 1]`, continue checking.
* If `arr[i] > arr[i + 1]`, the array is not sorted.
* Stop immediately and print `"Not Sorted"`.
* If the loop finishes without finding any violation, print `"Sorted"`.

---

# 🧠 Algorithm

1. Read the size of the array.
2. Read the array elements.
3. Traverse from index `0` to `n - 2`.
4. Compare `arr[i]` with `arr[i + 1]`.
5. If `arr[i] > arr[i + 1]`:

   * Print `"Not Sorted"`.
   * Stop the loop.
6. If the loop completes without `break`, print `"Sorted"`.

---

# 💻 Python Solution

```python
n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        print("Not Sorted")
        break
else:
    print("Sorted")
```

---

# ▶️ Dry Run

### Input

```text
5
1 2 4 3 5
```

| Iteration | Current | Next | Condition | Result     |
| --------- | ------: | ---: | --------- | ---------- |
| 1         |       1 |    2 | 1 ≤ 2     | Continue   |
| 2         |       2 |    4 | 2 ≤ 4     | Continue   |
| 3         |       4 |    3 | 4 > 3     | Not Sorted |

Output

```text
Not Sorted
```

---

# ⏱️ Complexity Analysis

## Time Complexity

### Best Case

The array is detected as unsorted in the first comparison.

```text
O(1)
```

### Average Case

The algorithm checks approximately half of the array before determining the result.

```text
O(n)
```

### Worst Case

The array is completely sorted, so every adjacent pair is checked.

```text
O(n)
```

---

## Space Complexity

Only the loop variable is used.

```text
O(1)
```

---

# 🎯 Key Concepts

* Array Traversal
* Adjacent Element Comparison
* Loop Control (`break`)
* `for...else` in Python
* Time Complexity
* Space Complexity

---

# 🚨 Edge Cases

### Already Sorted

Input

```text
5
1 2 3 4 5
```

Output

```text
Sorted
```

---

### Unsorted

Input

```text
5
5 4 3 2 1
```

Output

```text
Not Sorted
```

---

### Duplicate Elements

Input

```text
5
1 2 2 3 3
```

Output

```text
Sorted
```

---

### Single Element

Input

```text
1
100
```

Output

```text
Sorted
```

---

### All Elements Equal

Input

```text
4
7 7 7 7
```

Output

```text
Sorted
```

---

# 🧩 Pattern

**Pattern:** Array Traversal

The solution checks each pair of adjacent elements exactly once to verify whether the array maintains sorted order.

---

# 📚 Related Problems

* Bubble Sort
* Binary Search (requires a sorted array)
* Remove Duplicates from Sorted Array
* Merge Sorted Arrays
* Monotonic Array

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How to compare adjacent elements in an array.
* Why the loop runs until `n - 1`.
* How `break` exits a loop early.
* How Python's `for...else` works.
* Why checking sorted order takes **O(n)** time.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms

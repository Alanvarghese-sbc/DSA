# Remove Duplicates from Sorted Array

## 📌 Problem Statement

Given a sorted array, rearrange it in-place so that the first k positions contain only unique elements. Print the unique elements.

Print the array containing only the unique elements.

> **Note:** The array is already sorted in non-decreasing order.

---

# Example 1

### Input

```text
7
1 1 2 2 3 4 4
```

### Output

```text
1 2 3 4
```

### Explanation

The duplicate elements (`1`, `2`, and `4`) are removed, leaving only the unique elements.

---

# Example 2

### Input

```text
6
1 2 3 4 5 6
```

### Output

```text
1 2 3 4 5 6
```

### Explanation

There are no duplicate elements, so the array remains unchanged.

---

# Example 3

### Input

```text
5
2 2 2 2 2
```

### Output

```text
2
```

### Explanation

All elements are the same, so only one unique element remains.

---

# 💡 Approach

Since the array is already sorted, duplicate elements always appear next to each other.

Use the **Two Pointer** technique:

* `j` keeps track of the position of the last unique element.
* `i` traverses the array.
* Whenever a new unique element is found:

  * Increment `j`.
  * Copy the unique element to `arr[j]`.
* Finally, print the first `j + 1` elements.

This removes duplicates **in-place** without using any extra array.

---

# 🧠 Algorithm

1. Read the size of the array.
2. Read the sorted array.
3. Initialize `j = 0`.
4. Traverse the array from index `1` to `n - 1`.
5. If `arr[i]` is different from `arr[j]`:

   * Increment `j`.
   * Copy `arr[i]` to `arr[j]`.
6. Print the first `j + 1` elements.

---

# 💻 Python Solution

```python
n = int(input())

arr = list(map(int, input().split()))

j = 0

for i in range(1, n):
    if arr[j] != arr[i]:
        j += 1
        arr[j] = arr[i]

for num in range(j + 1):
    print(arr[num], end=" ")
```

---

# ▶️ Dry Run

### Input

```text
7
1 1 2 2 3 4 4
```

| Step  | `i` | `j` | Action             |
| ----- | --: | --: | ------------------ |
| Start |   - |   0 | `1 1 2 2 3 4 4`    |
| 1     |   1 |   0 | Duplicate → Ignore |
| 2     |   2 |   1 | Copy `2`           |
| 3     |   3 |   1 | Duplicate → Ignore |
| 4     |   4 |   2 | Copy `3`           |
| 5     |   5 |   3 | Copy `4`           |
| 6     |   6 |   3 | Duplicate → Ignore |

Final unique elements:

```text
1 2 3 4
```

---

# ⏱️ Complexity Analysis

## Time Complexity

### Best Case

Every element is checked exactly once.

```text
O(n)
```

### Average Case

Every element is checked once.

```text
O(n)
```

### Worst Case

Every element is checked once.

```text
O(n)
```

---

## Space Complexity

Only two integer variables (`i` and `j`) are used.

```text
O(1)
```

---

# 🎯 Key Concepts

* Arrays
* Two Pointers
* In-place Array Modification
* Sorted Arrays
* Duplicate Removal
* Time Complexity
* Space Complexity

---

# 🚨 Edge Cases

### No Duplicates

**Input**

```text
5
1 2 3 4 5
```

**Output**

```text
1 2 3 4 5
```

---

### All Duplicates

**Input**

```text
5
7 7 7 7 7
```

**Output**

```text
7
```

---

### Single Element

**Input**

```text
1
100
```

**Output**

```text
100
```

---

### Mixed Duplicates

**Input**

```text
8
1 1 2 3 3 4 5 5
```

**Output**

```text
1 2 3 4 5
```

---

# 🧩 Pattern

**Pattern:** Two Pointers

The algorithm uses two pointers:

* `i` → Traverses the array.
* `j` → Tracks the position of the last unique element.

This allows duplicate removal without using extra space.

---

# 📚 Related Problems

* Move Zeroes
* Merge Sorted Array
* Remove Element
* Squares of a Sorted Array
* Remove Duplicates from Sorted List

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How the Two Pointer technique works.
* Why sorted arrays make duplicate removal easier.
* How to modify an array in-place.
* Why this algorithm runs in **O(n)** time using **O(1)** extra space.
* How to solve similar in-place array manipulation problems.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms

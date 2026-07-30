# Merge Two Sorted Arrays

## 📌 Problem Statement

Given two **sorted arrays**, merge them into a single sorted array.

Print the merged sorted array.

> **Note:** Both input arrays are already sorted in non-decreasing order.

---

# Example 1

### Input

```text
5
1 3 5 7 9
4
2 4 6 8
```

### Output

```text
1 2 3 4 5 6 7 8 9
```

### Explanation

Both arrays are merged while maintaining the sorted order.

---

# Example 2

### Input

```text
3
1 2 3
3
4 5 6
```

### Output

```text
1 2 3 4 5 6
```

### Explanation

Since all elements of the first array are smaller, they appear before the elements of the second array.

---

# Example 3

### Input

```text
3
2 4 6
4
1 3 5 7
```

### Output

```text
1 2 3 4 5 6 7
```

### Explanation

The elements from both arrays are compared one by one to build the final sorted array.

---

# 💡 Approach

Since both arrays are already sorted, use the **Two Pointer** technique.

* Use pointer `i` for the first array.
* Use pointer `j` for the second array.
* Compare the current elements of both arrays.
* Append the smaller element to the result array.
* Move the corresponding pointer forward.
* After one array is exhausted, copy the remaining elements from the other array.

This ensures that the final array remains sorted.

---

# 🧠 Algorithm

1. Read the size and elements of the first sorted array.
2. Read the size and elements of the second sorted array.
3. Initialize:

   * `i = 0`
   * `j = 0`
   * `result = []`
4. Compare `arr1[i]` and `arr2[j]`.
5. Append the smaller element to `result`.
6. Move the corresponding pointer.
7. Repeat until one array is completely traversed.
8. Copy the remaining elements from the unfinished array.
9. Print the merged array.

---

# 💻 Python Solution

```python
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

i = 0
j = 0
result = []

while i < n and j < m:
    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

while i < n:
    result.append(arr1[i])
    i += 1

while j < m:
    result.append(arr2[j])
    j += 1

print(*result)
```

---

# ▶️ Dry Run

### Input

```text
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
```

| Step | `i` | `j` | Comparison         | Result      |
| ---- | --: | --: | ------------------ | ----------- |
| 1    |   0 |   0 | 1 < 2              | 1           |
| 2    |   1 |   0 | 3 > 2              | 1 2         |
| 3    |   1 |   1 | 3 < 4              | 1 2 3       |
| 4    |   2 |   1 | 5 > 4              | 1 2 3 4     |
| 5    |   2 |   2 | 5 < 6              | 1 2 3 4 5   |
| End  |   - |   - | Copy remaining `6` | 1 2 3 4 5 6 |

---

# ⏱️ Complexity Analysis

## Time Complexity

Every element from both arrays is visited exactly once.

```text
O(n + m)
```

where:

* `n` = size of the first array
* `m` = size of the second array

---

## Space Complexity

A new array is used to store the merged result.

```text
O(n + m)
```

---

# 🎯 Key Concepts

* Arrays
* Two Pointers
* Merging Sorted Arrays
* Array Traversal
* Time Complexity
* Space Complexity

---

# 🚨 Edge Cases

### One Array is Empty

**Input**

```text
0

3
1 2 3
```

**Output**

```text
1 2 3
```

---

### Both Arrays Have Same Elements

**Input**

```text
3
1 2 3
3
1 2 3
```

**Output**

```text
1 1 2 2 3 3
```

---

### Arrays of Different Sizes

**Input**

```text
5
1 3 5 7 9
2
2 4
```

**Output**

```text
1 2 3 4 5 7 9
```

---

### Single Element Arrays

**Input**

```text
1
5
1
3
```

**Output**

```text
3 5
```

---

# 🧩 Pattern

**Pattern:** Two Pointers

Two pointers (`i` and `j`) are used to traverse both sorted arrays simultaneously. At each step, the smaller element is added to the result, ensuring that the merged array remains sorted.

---

# 📚 Related Problems

* Merge Intervals
* Merge Sorted Linked Lists
* Merge Sort
* Intersection of Two Arrays
* Union of Two Sorted Arrays

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How the Two Pointer technique works with two arrays.
* How to merge two sorted arrays efficiently.
* Why the merge process runs in **O(n + m)** time.
* Why additional space is required for the merged array.
* How this algorithm forms the core of the **Merge Sort** algorithm.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms

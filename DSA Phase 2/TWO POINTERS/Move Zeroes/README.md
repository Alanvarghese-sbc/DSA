# Move Zeroes

## 📌 Problem Statement

Given an integer array, move all the **0's** to the **end** while maintaining the **relative order** of the non-zero elements.

The operation must be performed **in-place**, without creating another array.

---

## Example 1

### Input

```text
5
0 1 0 3 12
```

### Output

```text
1 3 12 0 0
```

---

## Example 2

### Input

```text
5
1 2 3 4 5
```

### Output

```text
1 2 3 4 5
```

### Explanation

There are no zeroes, so the array remains unchanged.

---

## Example 3

### Input

```text
5
0 0 0 0 0
```

### Output

```text
0 0 0 0 0
```

### Explanation

All elements are zero, so the array remains unchanged.

---

# 💡 Approach

Use the **Two Pointer** technique.

* `i` traverses the array from left to right.
* `j` points to the position where the next non-zero element should be placed.

Whenever a non-zero element is found:

1. Swap `arr[i]` with `arr[j]`.
2. Increment `j`.

By the end of the traversal:

* All non-zero elements are moved to the front.
* All zeroes automatically move to the end.
* The relative order of non-zero elements is preserved.

---

# 🧠 Algorithm

1. Read the array.
2. Initialize `j = 0`.
3. Traverse the array using index `i`.
4. If `arr[i]` is not zero:

   * Swap `arr[i]` and `arr[j]`.
   * Increment `j`.
5. Print the modified array.

---

# 💻 Python Solution

```python
n = int(input())

arr = list(map(int, input().split()))

j = 0

for i in range(n):
    if arr[i] != 0:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        j += 1

print(*arr)
```

---

# ▶️ Dry Run

### Input

```text
0 1 0 3 12
```

| i | j | Array      |
| - | - | ---------- |
| 0 | 0 | 0 1 0 3 12 |
| 1 | 0 | 1 0 0 3 12 |
| 2 | 1 | 1 0 0 3 12 |
| 3 | 1 | 1 3 0 0 12 |
| 4 | 2 | 1 3 12 0 0 |

Final Output

```text
1 3 12 0 0
```

---

# ⏱️ Complexity Analysis

## Time Complexity

The array is traversed only once.

```text
O(n)
```

---

## Space Complexity

Only three extra variables are used:

* `i`
* `j`
* `temp`

Therefore,

```text
O(1)
```

---

# 🎯 Key Concepts

* Arrays
* Two Pointer Technique
* In-place Algorithm
* Swapping
* Array Traversal
* Time Complexity
* Space Complexity

---

# 🚨 Edge Cases

### No Zeroes

Input

```text
1 2 3 4 5
```

Output

```text
1 2 3 4 5
```

---

### All Zeroes

Input

```text
0 0 0 0
```

Output

```text
0 0 0 0
```

---

### Single Element

Input

```text
1
0
```

Output

```text
0
```

---

### Zero at the End

Input

```text
1 2 3 0
```

Output

```text
1 2 3 0
```

---

# 🧩 Pattern

**Pattern:** Two Pointers

The Two Pointer technique uses two indices that move through the array to solve problems efficiently without using extra memory.

---

# 📚 Related Problems

* Reverse Array
* Remove Duplicates from Sorted Array
* Remove Element
* Sort Colors
* Rotate Array
* Squares of a Sorted Array

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How the Two Pointer technique works.
* How to perform an in-place array modification.
* How swapping helps preserve the order of non-zero elements.
* Why the solution runs in **O(n)** time and uses **O(1)** extra space.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms

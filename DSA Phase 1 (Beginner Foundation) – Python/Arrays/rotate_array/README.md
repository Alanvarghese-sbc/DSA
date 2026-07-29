# Rotate Array (Right Rotation)

## 📌 Problem Statement

Given an integer array and an integer `k`, rotate the array to the **right** by `k` positions.

The rotation must be performed **in-place** without using extra arrays or built-in rotation methods.

---

## Example 1

### Input

```text
7
1 2 3 4 5 6 7
3
```

### Output

```text
5 6 7 1 2 3 4
```

---

## Example 2

### Input

```text
5
10 20 30 40 50
2
```

### Output

```text
40 50 10 20 30
```

---

## Example 3

### Input

```text
5
1 2 3 4 5
7
```

### Output

```text
4 5 1 2 3
```

### Explanation

Since the array length is `5`:

```text
7 % 5 = 2
```

Rotating the array 7 times is equivalent to rotating it 2 times.

---

# 💡 Approach

This solution uses the **Reversal Algorithm**, an efficient in-place technique for rotating an array.

The algorithm consists of three steps:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n-k` elements.

Using a helper function avoids code duplication and makes the solution easier to understand and maintain.

---

# 🧠 Algorithm

1. Read the array and the value of `k`.
2. Compute `k = k % n`.
3. Reverse the entire array.
4. Reverse the first `k` elements.
5. Reverse the remaining elements.
6. Print the rotated array.

---

# 💻 Python Solution

```python
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

k = k % n

def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

reverse(arr, 0, n - 1)
reverse(arr, 0, k - 1)
reverse(arr, k, n - 1)

print(*arr)
```

---

# ▶️ Dry Run

### Input

```text
1 2 3 4 5 6 7
k = 3
```

### Step 1 – Reverse Entire Array

```text
7 6 5 4 3 2 1
```

---

### Step 2 – Reverse First `k` Elements

```text
5 6 7 4 3 2 1
```

---

### Step 3 – Reverse Remaining Elements

```text
5 6 7 1 2 3 4
```

Final Output

```text
5 6 7 1 2 3 4
```

---

# ⏱️ Complexity Analysis

## Time Complexity

Three reverse operations are performed.

```text
O(n) + O(k) + O(n-k)
```

Simplifying,

```text
O(n)
```

---

## Space Complexity

The algorithm uses only a few extra variables.

```text
O(1)
```

---

# 🎯 Key Concepts

* Arrays
* Two Pointers
* Reversal Algorithm
* Functions
* In-place Array Manipulation
* Modulo Operation (`k % n`)
* Time & Space Complexity

---

# 🚨 Edge Cases

### Rotate by Zero

Input

```text
5
1 2 3 4 5
0
```

Output

```text
1 2 3 4 5
```

---

### Rotate by Array Length

Input

```text
5
1 2 3 4 5
5
```

Output

```text
1 2 3 4 5
```

---

### Rotate More Than Array Length

Input

```text
5
1 2 3 4 5
12
```

Output

```text
4 5 1 2 3
```

---

### Single Element

Input

```text
1
10
8
```

Output

```text
10
```

---

# 🧩 Pattern

**Pattern:** Two Pointers (Reversal Technique)

The Reversal Algorithm is an optimized approach that rotates an array in-place using three reverse operations, achieving **O(n)** time and **O(1)** extra space.

---

# 📚 Related Problems

* Reverse Array
* Move Zeroes
* Rotate String
* Reverse Words in a String
* Next Permutation
* Spiral Matrix

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How to rotate an array efficiently without extra memory.
* Why `k % n` is necessary.
* How helper functions improve code readability.
* How the Reversal Algorithm works.
* How to solve array rotation in **O(n)** time and **O(1)** space.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms

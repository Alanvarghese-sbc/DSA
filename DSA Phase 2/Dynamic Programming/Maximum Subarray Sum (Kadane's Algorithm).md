# Maximum Subarray Sum (Kadane's Algorithm)

## 📌 Problem Statement

Given an integer array (which may contain both positive and negative numbers), find the **maximum possible sum of a contiguous subarray**.

Print the maximum subarray sum.

---

# Example 1

### Input

```text
8
-2 -3 4 -1 -2 1 5 -3
```

### Output

```text
7
```

### Explanation

The maximum sum subarray is:

```text
4 -1 -2 1 5
```

Sum:

```text
7
```

---

# Example 2

### Input

```text
5
1 2 3 4 5
```

### Output

```text
15
```

---

# Example 3

### Input

```text
5
-5 -2 -8 -1 -10
```

### Output

```text
-1
```

The largest subarray contains only `-1`.

---

# 💡 Approach

Use **Kadane's Algorithm**.

Maintain two variables:

* **current_sum** → Maximum sum ending at the current index.
* **maximum_sum** → Maximum sum found so far.

At every element, decide whether to:

* Continue the current subarray.
* Start a new subarray from the current element.

Update the answer whenever a larger sum is found.

---

# 🧠 Algorithm

1. Initialize `current_sum` and `maximum_sum` with the first element.
2. Traverse the array from the second element.
3. If extending the current subarray gives a larger sum, continue it.
4. Otherwise, start a new subarray from the current element.
5. Update the maximum sum.
6. Print the maximum sum.

---

# 💻 Python Solution (Using if-else)

```python
n = int(input())

arr = list(map(int, input().split()))

current_sum = arr[0]
maximum_sum = arr[0]

for i in range(1, n):

    if current_sum + arr[i] > arr[i]:
        current_sum += arr[i]
    else:
        current_sum = arr[i]

    if current_sum > maximum_sum:
        maximum_sum = current_sum

print(maximum_sum)
```

---

# 💻 Python Solution (Using max())

```python
n = int(input())

arr = list(map(int, input().split()))

current_sum = arr[0]
maximum_sum = arr[0]

for i in range(1, n):
    current_sum = max(current_sum + arr[i], arr[i])
    maximum_sum = max(maximum_sum, current_sum)

print(maximum_sum)
```

---

# ▶️ Dry Run

### Input

```text
-2 -3 4 -1 -2 1 5 -3
```

| Element | Current Sum | Maximum Sum |
| ------: | ----------: | ----------: |
|      -2 |          -2 |          -2 |
|      -3 |          -3 |          -2 |
|       4 |           4 |           4 |
|      -1 |           3 |           4 |
|      -2 |           1 |           4 |
|       1 |           2 |           4 |
|       5 |           7 |           7 |
|      -3 |           4 |           7 |

Output:

```text
7
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

Only two variables are maintained.

```text
O(1)
```

---

# 🎯 Key Concepts

* Arrays
* Kadane's Algorithm
* Dynamic Programming
* Greedy Choice
* Array Traversal

---

# 🚨 Edge Cases

### All Positive Numbers

**Input**

```text
1 2 3 4 5
```

**Output**

```text
15
```

---

### All Negative Numbers

**Input**

```text
-5 -2 -8 -1
```

**Output**

```text
-1
```

---

### Single Element

**Input**

```text
5
```

**Output**

```text
5
```

---

### Mixed Positive and Negative

**Input**

```text
3 -2 5 -1
```

**Output**

```text
6
```

---

# 🧩 Pattern

**Pattern:** Dynamic Programming / Kadane's Algorithm

At every index, choose the better of:

* Continue the current subarray.
* Start a new subarray.

This local optimal choice leads to the global optimum.

---

# 📚 Related Problems

* Maximum Product Subarray
* Circular Maximum Subarray Sum
* Best Time to Buy and Sell Stock
* House Robber
* Longest Increasing Subsequence

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How Kadane's Algorithm works.
* How to optimize from **O(n²)** to **O(n)**.
* Why restarting the subarray can produce a better result.
* The relationship between greedy decisions and dynamic programming.
* How to solve one of the most frequently asked array interview problems.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms

# Find Missing Number

## 📌 Problem Statement

Given an array containing **n - 1 distinct integers** from the range **1 to n**, find the missing number.

Print the missing number.

> **Note:** Exactly one number is missing from the sequence.

---

# Example 1

### Input

```text
5
1 2 4 5
```

### Output

```text
3
```

### Explanation

The numbers should be from `1` to `5`. Since `3` is missing, the output is `3`.

---

# Example 2

### Input

```text
6
2 3 1 6 5
```

### Output

```text
4
```

### Explanation

The numbers should be from `1` to `6`. The missing number is `4`.

---

# Example 3

### Input

```text
4
2 3 4
```

### Output

```text
1
```

### Explanation

The first number of the sequence is missing.

---

# 💡 Approach

The sum of numbers from `1` to `n` can be calculated using the formula:

```text
n × (n + 1) / 2
```

Calculate:

* **Expected Sum** → Sum of numbers from `1` to `n`
* **Actual Sum** → Sum of the given array elements

The difference between these two sums is the missing number.

---

# 🧠 Algorithm

1. Read the value of `n`.

2. Read the array containing `n - 1` elements.

3. Calculate the expected sum using:

   ```python
   expected_sum = n * (n + 1) // 2
   ```

4. Traverse the array and calculate the actual sum.

5. Find the missing number:

   ```python
   missing_number = expected_sum - actual_sum
   ```

6. Print the missing number.

---

# 💻 Python Solution

```python
n = int(input())

arr = list(map(int, input().split()))

expected_sum = n * (n + 1) // 2

actual_sum = 0

for num in arr:
    actual_sum += num

missing_number = expected_sum - actual_sum

print(missing_number)
```

---

# ▶️ Dry Run

### Input

```text
5
1 2 4 5
```

Expected Sum

```text
1 + 2 + 3 + 4 + 5 = 15
```

Actual Sum

```text
1 + 2 + 4 + 5 = 12
```

Missing Number

```text
15 - 12 = 3
```

Output

```text
3
```

---

# ⏱️ Complexity Analysis

## Time Complexity

The array is traversed only once to calculate the sum.

```text
O(n)
```

---

## Space Complexity

Only a few integer variables are used.

```text
O(1)
```

---

# 🎯 Key Concepts

* Arrays
* Array Traversal
* Mathematical Formula
* Summation
* Time Complexity
* Space Complexity

---

# 🚨 Edge Cases

### Missing First Number

**Input**

```text
5
2 3 4 5
```

**Output**

```text
1
```

---

### Missing Last Number

**Input**

```text
5
1 2 3 4
```

**Output**

```text
5
```

---

### Single Missing Value

**Input**

```text
2
2
```

**Output**

```text
1
```

---

### Larger Example

**Input**

```text
8
1 2 3 5 6 7 8
```

**Output**

```text
4
```

---

# 🧩 Pattern

**Pattern:** Array Traversal / Mathematical Formula

The solution computes the expected sum of the complete sequence and subtracts the sum of the given elements to determine the missing number.

---

# 📚 Related Problems

* Missing Number (LeetCode 268)
* Find the Duplicate Number
* Find All Numbers Disappeared in an Array
* First Missing Positive
* Missing and Repeating Number

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How to use mathematical formulas to simplify a problem.
* How to calculate the sum of an array using a loop.
* Why this solution runs in **O(n)** time.
* Why only **O(1)** extra space is required.
* How mathematical optimization can replace additional data structures.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms

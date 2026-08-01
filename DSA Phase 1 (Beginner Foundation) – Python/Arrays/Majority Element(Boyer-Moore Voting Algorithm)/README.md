# Majority Element (Boyer-Moore Voting Algorithm)

## 📌 Problem Statement

Given an integer array of size **n**, find the **majority element**.

A **majority element** is an element that appears **more than `n // 2` times**.

You may assume that the majority element always exists.

Print the majority element.

---

# Example 1

### Input

```text
7
2 2 1 1 2 2 2
```

### Output

```text
2
```

### Explanation

The element `2` appears **5 times**, which is more than `7 // 2 = 3`.

---

# Example 2

### Input

```text
5
3 3 4 2 3
```

### Output

```text
3
```

### Explanation

The element `3` appears **3 times**, which is more than `5 // 2 = 2`.

---

# Example 3

### Input

```text
9
1 1 2 1 3 1 1 4 1
```

### Output

```text
1
```

---

# 💡 Approach

Use the **Boyer-Moore Voting Algorithm**.

Maintain two variables:

* **candidate** → The current majority candidate.
* **count** → The vote count for the candidate.

### Voting Rules

* If `count == 0`, choose the current element as the new candidate.
* If the current element is the candidate, increase the vote count.
* Otherwise, decrease the vote count.

Since the majority element appears more than half of the time, it cannot be completely canceled by other elements.

---

# 🧠 Algorithm

1. Initialize:

   * `candidate = None`
   * `count = 0`
2. Traverse the array.
3. If `count == 0`:

   * Set the current element as the candidate.
   * Set `count = 1`.
4. Else if the current element equals the candidate:

   * Increment `count`.
5. Otherwise:

   * Decrement `count`.
6. After the traversal, print the candidate.

---

# 💻 Python Solution

```python
n = int(input())

arr = list(map(int, input().split()))

candidate = None
count = 0

for i in range(n):

    if count == 0:
        candidate = arr[i]
        count = 1

    elif arr[i] == candidate:
        count += 1

    else:
        count -= 1

print(candidate)
```

---

# ▶️ Dry Run

### Input

```text
2 2 1 1 2 2 2
```

| Element | Candidate | Count |
| ------: | --------: | ----: |
|       2 |         2 |     1 |
|       2 |         2 |     2 |
|       1 |         2 |     1 |
|       1 |         2 |     0 |
|       2 |         2 |     1 |
|       2 |         2 |     2 |
|       2 |         2 |     3 |

Output

```text
2
```

---

# 🧠 Why Does It Work?

Think of every occurrence of the majority element as a **positive vote**.

Every different element cancels one vote.

Since the majority element appears more than **n // 2** times, it will always have votes remaining after all cancellations.

Therefore, the final candidate is the majority element.

---

# ⏱️ Complexity Analysis

## Time Complexity

The array is traversed only once.

```text
O(n)
```

---

## Space Complexity

Only two variables are used.

```text
O(1)
```

---

# 🎯 Key Concepts

* Arrays
* Boyer-Moore Voting Algorithm
* Greedy Algorithm
* Candidate Elimination
* Constant Space Algorithm

---

# 🚨 Edge Cases

### Majority at the Beginning

**Input**

```text
5
1 1 1 2 3
```

**Output**

```text
1
```

---

### Majority at the End

**Input**

```text
7
2 3 1 4 5 5 5 5
```

**Output**

```text
5
```

---

### All Elements Same

**Input**

```text
4
7 7 7 7
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
10
```

**Output**

```text
10
```

---

# 🧩 Pattern

**Pattern:** Boyer-Moore Voting Algorithm / Greedy

Repeatedly eliminate pairs of different elements. Since the majority element occurs more than half the time, it cannot be completely canceled and remains as the final candidate.

---

# 📚 Related Problems

* Majority Element II
* Find All Elements Appearing More Than n/3 Times
* First Non-Repeating Element
* Top K Frequent Elements
* Frequency Count

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How the Boyer-Moore Voting Algorithm works.
* Why candidate elimination correctly identifies the majority element.
* How to solve the problem in **O(n)** time and **O(1)** space.
* Why this approach is more efficient than using a hash map for this specific problem.

> **Note:** If the problem does **not** guarantee that a majority element exists, perform a second traversal to count the occurrences of the final candidate. If its frequency is greater than `n // 2`, it is the majority element; otherwise, no majority element exists.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms

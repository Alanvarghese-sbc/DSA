# 🚀 Phase 2: DSA Patterns (Python)

This phase focuses on identifying and solving common problem-solving patterns used in coding interviews.

---

## 🎯 Goal

* Move from brute force → optimized solutions
* Recognize patterns quickly
* Improve time complexity

---

## 🧠 Patterns Covered

---

## 1️⃣ Hashing (Dictionary)

### 📌 Concept

Store and lookup data in O(1) time using a dictionary.

### 🔑 Use Cases

* Frequency count
* Duplicate detection
* Grouping elements

### 💻 Example

```python
nums = [1,2,2,3,1]

freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)
```

### ⏱ Complexity

* Time: O(n)
* Space: O(n)

---

## 2️⃣ Prefix Sum

### 📌 Concept

Precompute cumulative sums to avoid repeated calculations.

### 🔑 Use Cases

* Range sum queries
* Distance calculations
* Subarray problems

### 💻 Example

```python
nums = [1,2,3,4]

prefix = [0]
for num in nums:
    prefix.append(prefix[-1] + num)

print(prefix)  # [0,1,3,6,10]
```

### ⏱ Complexity

* Time: O(n)
* Space: O(n)

---

## 3️⃣ Two Pointers

### 📌 Concept

Use two indices to traverse array efficiently.

### 🔑 Use Cases

* Sorted arrays
* Pair problems
* Removing duplicates

### 💻 Example

```python
arr = [1,2,3,4,5]
left = 0
right = len(arr) - 1

while left < right:
    print(arr[left], arr[right])
    left += 1
    right -= 1
```

---

## 4️⃣ Sliding Window

### 📌 Concept

Maintain a window of elements and slide it across array.

### 🔑 Use Cases

* Subarray sum
* Longest substring
* Fixed/variable window

### 💻 Example

```python
arr = [1,2,3,4,5]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)

print(max_sum)
```

---

## 5️⃣ Sorting + Greedy

### 📌 Concept

Sort data and make locally optimal choices.

### 🔑 Use Cases

* Minimum/maximum problems
* Interval scheduling
* Resource allocation

### 💻 Example

```python
arr = [4,2,1,3]
arr.sort()
print(arr)
```

---

## 6️⃣ Matrix Traversal

### 📌 Concept

Traverse 2D arrays using row/column logic.

### 🔑 Use Cases

* Spiral traversal
* Boundary traversal
* Grid problems

### 💻 Example

```python
matrix = [
    [1,2],
    [3,4]
]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j])
```

---

## 🔥 Important Notes

* Always start with brute force
* Then identify pattern
* Then optimize

---

## 🚀 Next Step

Solve problems based on each pattern:

* Hashing → Two Sum
* Prefix Sum → Subarray sum
* Two Pointers → Pair sum
* Sliding Window → Maximum subarray of size k

---

## 🧠 Key Learning

Understanding patterns is more important than solving many problems.

---

## 👨‍💻 Author

Alan Varghese

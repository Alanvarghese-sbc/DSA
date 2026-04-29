# 🌀 Spiral Matrix Traversal (Single-Line Input | Python)

## 📌 Problem Statement

Given a matrix in a **single-line input format**, print all elements in **spiral order**.

Spiral traversal follows this pattern:

* Left → Right
* Top → Bottom
* Right → Left
* Bottom → Top  
(Repeat until all elements are visited)

---

## 📥 Input Format

A single line containing:

n m a1 a2 a3 ... a(n*m)


Where:
- `n` = number of rows  
- `m` = number of columns  
- Remaining values = matrix elements (row-wise)

---

## 📤 Output Format

Print all elements of the matrix in **spiral order** (space-separated).

---

## 🧾 Example

### Input:
3 3 1 2 3 4 5 6 7 8 9


### Matrix Form:
1 2 3
4 5 6
7 8 9


### Output:
1 2 3 6 9 8 7 4 5


---

## 🧠 Approach

### Step 1: Parse Input

- Read all values into a list
- Extract:
  - `n`, `m`
  - Remaining values → matrix elements

---

### Step 2: Convert 1D List → 2D Matrix

```python
matrix = [values[i*m:(i+1)*m] for i in range(n)]
👉 This slices the list into rows of size m
```

### Step 3: Spiral Traversal
Use 4 boundaries:

top → first row

bottom → last row

left → first column

right → last column

Traversal Order:
Left → Right → top += 1

Top → Bottom → right -= 1

Right → Left → bottom -= 1

Bottom → Top → left += 1

Repeat until:

top > bottom OR left > right
⚠️ Important Conditions
if top <= bottom
if left <= right
👉 These prevent:

Duplicate traversal

Index errors

Issues in single row/column cases

### 💻 Python Code
```
data = list(map(int, input().split()))

n = data[0]
m = data[1]
values = data[2:]

# Convert to matrix
matrix = [values[i*m:(i+1)*m] for i in range(n)]

top, bottom = 0, n-1
left, right = 0, m-1

result = []

while top <= bottom and left <= right:
    
    # Top row
    for i in range(left, right+1):
        result.append(matrix[top][i])
    top += 1

    # Right column
    for i in range(top, bottom+1):
        result.append(matrix[i][right])
    right -= 1

    # Bottom row
    if top <= bottom:
        for i in range(right, left-1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    # Left column
    if left <= right:
        for i in range(bottom, top-1, -1):
            result.append(matrix[i][left])
        left += 1

print(*result)

```

### ⏱ Time & Space Complexity
Time Complexity: O(n × m)

Space Complexity: O(n × m) (for result list)

### 🔥 Key Concepts
Matrix traversal

List slicing

Boundary shrinking

Input parsing (single-line format)

### ⚠️ Edge Cases
Single row (1 x m)

Single column (n x 1)

Invalid input length (len(values) != n*m)

### 🚀 Related Problems
Reverse Spiral Traversal

Boundary Traversal

Rotate Matrix 90°

Zigzag Traversal

### 📌 Author
Alan Varghese
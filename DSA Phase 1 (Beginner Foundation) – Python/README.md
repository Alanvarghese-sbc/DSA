# 🚀 DSA Phase 1 (Beginner Foundation) – Python

## 👨‍💻 Overview

This phase focuses on building a strong foundation in **programming and problem-solving** using Python.
The goal is to develop **logic-building skills** before moving to advanced Data Structures and Algorithms.

---

## 🎯 Objectives

* Understand basic programming concepts
* Build logical thinking
* Solve beginner-level problems confidently
* Learn basics of time and space complexity

---

## 🧠 Concepts Covered

### 1. Basic Programming

#### Input / Output

```python
name = input("Enter your name: ")
print("Hello", name)
```

#### Variables and Data Types

* int, float, string, boolean

---

### 2. Conditional Statements

#### If-Else

```python
num = int(input())

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### 3. Loops

#### For Loop

```python
for i in range(5):
    print(i)
```

#### While Loop

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## 📦 Arrays (Lists in Python)

### 🔹 Definition

A list is a collection of elements stored in a single variable.

```python
arr = [1, 2, 3, 4, 5]
```

---

### 🔹 Operations

#### Traversal

```python
for i in arr:
    print(i)
```

#### Find Maximum

```python
max_val = arr[0]
for i in arr:
    if i > max_val:
        max_val = i
```

#### Sum of Elements

```python
total = sum(arr)
```

#### Reverse List

```python
arr.reverse()
```

---

## 🔤 Strings

### 🔹 Definition

A string is a sequence of characters.

```python
s = "hello"
```

---

### 🔹 Operations

#### Reverse String

```python
s = s[::-1]
```

#### Palindrome Check

```python
if s == s[::-1]:
    print("Palindrome")
```

#### Count Characters

```python
count = {}
for char in s:
    count[char] = count.get(char, 0) + 1
```

---

## 🧠 Complexity Basics

### 🔹 Time Complexity

Measures how fast an algorithm runs.

#### Types:

* O(1) → Constant
* O(n) → Linear
* O(n²) → Quadratic
* O(log n) → Logarithmic

---

### 🔹 Space Complexity

Measures how much extra memory is used.

* O(1) → Constant
* O(n) → Linear

---

### 🔹 Example

```python
for i in range(n):
    print(i)
```

Time Complexity: O(n)
Space Complexity: O(1)

---

## 🧩 Problem Solving Approach

1. Understand the problem
2. Identify input and output
3. Think of a simple solution
4. Write code
5. Optimize if needed

---

## 🧪 Practice Platform

* HackerRank (Python Track)

  * Basic Data Types
  * If-Else
  * Loops
  * Lists
  * Strings

---

## 📅 Daily Practice Plan

* Solve 5–8 problems daily
* Focus on understanding logic
* Analyze time and space complexity

---

## ⚡ Key Learnings

* Logic is more important than syntax
* Practice is essential
* Start simple, then improve
* Consistency is the key

---

## ❌ Topics Not Covered in Phase 1

* Linked List
* Stack & Queue
* Trees
* Graphs
* Dynamic Programming

---

## 🚀 Next Phase

After completing this phase:

* Start learning C++
* Move to core Data Structures
* Begin solving intermediate problems

---

## 📌 Status

* Beginner Phase
* Building strong foundation
* Preparing for advanced DSA

---

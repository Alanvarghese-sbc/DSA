# n,m = map(int, input().split())

# matrix = []

# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

data = list(map(int, input().split()))
n = data[0]
m = data[1]

values = data[2:]

matrix = [
    values[i * m:(i + 1) * m]
    for i in range(n)
]


top = 0
bottom = n - 1
left = 0
right = m - 1

result = []

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(*result)
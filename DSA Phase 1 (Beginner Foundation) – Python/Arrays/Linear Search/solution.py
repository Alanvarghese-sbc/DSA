n = int(input())

arr = list(map(int, input().split()))

target = int(input())

is_found = False

for i in range(n):
    if arr[i] == target:
        is_found = True
        print(i)
        break

if not is_found:
    print(-1)


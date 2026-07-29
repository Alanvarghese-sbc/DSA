n = int(input())

arr = list(map(int, input().split()))

target = int(input())

left = 0
right = n-1

while left <= right:
    mid = (left+right)//2
    if arr[mid] == target:
        found = True
        print(mid)
    elif arr[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
else:
    print(-1)
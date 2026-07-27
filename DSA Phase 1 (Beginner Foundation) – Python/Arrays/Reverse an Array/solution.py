n = int(input())

arr = list(map(int, input().split()))

left = 0
right = n-1

while left <= right:
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left+=1
    right-=1

print(*arr)

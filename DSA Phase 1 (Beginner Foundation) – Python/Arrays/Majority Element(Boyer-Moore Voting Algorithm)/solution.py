n = int(input())
arr = list(map(int, input().split()))

candidate = None
count = 0

for i in range(n):
    if count == 0:
        candidate = arr[i]
        count+=1
    elif arr[i] == candidate:
        count+=1
    else:
        count-=1

print(candidate)
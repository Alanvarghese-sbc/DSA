n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1):
    if arr[i] > arr[i+1]:
        print("Not Sorted")
        break
else:
    print("Sorted")

        


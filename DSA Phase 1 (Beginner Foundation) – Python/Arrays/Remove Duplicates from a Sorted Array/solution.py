n = int(input())

arr = list(map(int, input().split()))

j=0                                                                                             

for i in range(1,n):
    if arr[j] != arr[i]:
        j+=1
        arr[j] = arr[i]

for num in range(j+1):
    print(arr[num],end=" ")
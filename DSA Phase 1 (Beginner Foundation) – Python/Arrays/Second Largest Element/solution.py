n = int(input())

arr = list(map(int, input().split()))

largest = float('-inf')
second_Largest = float('-inf')

for num in arr:
    if num > largest :
        second_Largest = largest
        largest = num
    elif num > second_Largest and num != largest:
        second_Largest = num

if second_Largest == float('-inf'):
    print(-1)
else:
    print(second_Largest)


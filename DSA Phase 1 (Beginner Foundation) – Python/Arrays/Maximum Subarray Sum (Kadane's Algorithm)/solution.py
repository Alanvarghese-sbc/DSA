n = int(input())

arr = list(map(int, input().split()))

current_sum = arr[0]
maximum_sum = arr[0]

for i in range(1,n):
    if current_sum+arr[i] > arr[i]:
        current_sum = current_sum+arr[i]
    else:
        current_sum=arr[i]

    if current_sum > maximum_sum:
        maximum_sum = current_sum

# for i in range(1, n):
#     current_sum = max(current_sum + arr[i], arr[i])
#     maximum_sum = max(maximum_sum, current_sum)

print(maximum_sum)




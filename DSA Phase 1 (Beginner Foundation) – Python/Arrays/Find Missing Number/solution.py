n = int(input())

arr = list(map(int, input().split()))

exp_sum = n*(n+1)//2

actual_sum = 0

for num in arr:
    actual_sum += num

missing_number = exp_sum - actual_sum

print(missing_number)
n = int(input())
arr = list(map(int,input().split()))

minimum_price = arr[0]
max_profit = 0

for i in range(1,n):
    if arr[i] < minimum_price:
        minimum_price = arr[i]
    else:
        profit = arr[i] - minimum_price
        if profit > max_profit:
            max_profit = profit

print(max_profit)


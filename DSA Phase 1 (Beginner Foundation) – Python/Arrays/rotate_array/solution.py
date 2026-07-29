n = int(input())
arr = list(map(int, input().split()))
k = int(input())

k = k%n

def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1

left = 0
right = n-1



#reversing the array first
# while left < right:
#     temp = arr[left]
#     arr[left] = arr[right]
#     arr[right] = temp
#     left+=1
#     right-=1 
reverse(arr, left, right)


left = 0
right = k-1

# Reverse first k elements

# while left < right:
#     temp = arr[left]
#     arr[left] = arr[right]
#     arr[right] = temp
#     left+=1
#     right-=1

reverse(arr,left,right)

left = k
right = n-1

# Reverse remaining elements

# while left < right:
#     temp = arr[left]
#     arr[left] = arr[right]
#     arr[right] = temp
#     left+=1
#     right-=1

reverse(arr, left, right)

print(*arr)


n = int(input())
arr = list(map(int, input().split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

found = False

# for k in freq:
#     if freq[k] == 1:
#         print(k)
#         found = True
#         break

# or

for n in arr:
    if freq[n] == 1:
        print(n)
        found = True
        break

if not found:
    print(-1)

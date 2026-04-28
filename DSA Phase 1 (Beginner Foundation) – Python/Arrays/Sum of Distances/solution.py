def distance(nums):
    n = len(nums)
    result = [0] * n

    for i in range(n):
        total = 0
        for j in range(n):
            if i != j and nums[i] == nums[j]:
                total += abs(i - j)
        result[i] = total

    return result


# Example
nums = [1,3,1,1,2]
print(distance(nums))

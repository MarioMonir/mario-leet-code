nums = [1,2,3,4]


# Faster
def runningSum(nums):
    sums = 0
    for i in range(len(nums)):
        sums += nums[i]
        nums[i] = sums
    return nums


def runningSum2(nums):
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums



print(runningSum(nums))

print("-"*30)

nums = [1,2,3,4]
print(runningSum2(nums))


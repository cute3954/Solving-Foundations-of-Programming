# https://codingbat.com/prob/p158767
# Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.
#
# canBalance([1, 1, 1, 2, 1]) → true
# canBalance([2, 1, 1, 2, 1]) → false
# canBalance([10, 10]) → true

nums = list(map(int, input().split()))
total = sum(nums)
leftsum = 0
result = False

if len(nums) > 1:
    for i in range(len(nums)):
        leftsum += nums[i]
        if leftsum == total / 2:
            break
    rightsum = total - leftsum
    if leftsum == rightsum:
        result = True

print(result)
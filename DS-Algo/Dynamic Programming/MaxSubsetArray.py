'''
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

For example, given an array arr = [-2, 1, 3, -4, 5] we have the following possible subsets:

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8

Our maximum subset sum is 8.

'''

def maxSubsetSum(arr):
    dp = {} 
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])
    for i, num in enumerate(arr[2:], start=2):
        dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2], num)
    return dp[len(arr)-1]

n = int(input("Enter number values in the array: "))
arr = list(map(int, input("Enter values of the array: ").rstrip().split()))
res = maxSubsetSum(arr)
print("Maximum Subset sum array is: "+str(res))
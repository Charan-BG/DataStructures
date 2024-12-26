"""
Coding Exercise: Target Sum
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer 
in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1], target = 2
Output: 4
Explanation: There are 4 ways to assign symbols to make the sum of nums be target 2.
-1 + 1 + 1 + 1  = 2
+1 - 1 + 1 + 1  = 2
+1 + 1 - 1 + 1  = 2
+1 + 1 + 1 - 1  = 2
"""

def target_sum(nums, target):

    total_sum=sum(nums)
    print(total_sum)

    if (total_sum+target)%2 !=0 or total_sum < abs(target):
        return 0
    
    subset_sum=(target+total_sum)//2

    dp=[0]*(subset_sum+1)
    dp[0]=1

    for num in nums:
        for j in range(subset_sum, num-1, -1):

            dp[j]+=dp[j-num]

    return dp[subset_sum]

nums = [1,1,1,1]; target = 2
nums = [1,1,3]
target = 5

print(target_sum(nums, target))

# Expected Output: 3
# Explanation: Three combinations achieve the target sum.
# +1 + 2 + 3 - 4 - 5 = 5
# +1 - 2 + 3 + 4 - 5 = 5
# -1 + 2 + 3 + 4 - 5 = 5

# nums = [1, 2, 3]
# target = -1
# # Expected Output: 1
# # Explanation: One combination exists to achieve the target sum.
# # -1 + 2 - 3 = -1

# nums = [1, 1, 2, 3]
# target = 0
# # Expected Output: 3
# # Explanation: Three combinations exist to achieve the target sum.

# nums = [1, 2, 3]
# target = 7
# # Expected Output: 0
# # Explanation: No combination of signs can produce a sum of 7.

# nums = [1] * 20
# target = 10
# # Expected Output: Computed based on the logic. Verify via function execution.

# nums = [5]
# target = 5
# # Expected Output: 1
# # Explanation: Only one valid expression: +5.

# nums = [5]
# target = 3
# # Expected Output: 0
# # Explanation: No valid combinations can achieve the target sum.

# nums = [2, 3, 7, 8, 10]
# target = 5
# # Expected Output: 2
# # Explanation: Two valid combinations exist.
# nums = [1] * 20
# target = 10
# # Expected Output: Computed based on the logic. Verify via function execution.
# nums = [1, 2, 3]
# target = -1
# # Expected Output: 1
# # Explanation: One combination exists to achieve the target sum.
# # -1 + 2 - 3 = -1

# nums = [1, 1, 2, 3]
# target = 0
# # Expected Output: 3
# # Explanation: Three combinations exist to achieve the target sum.

# print(target_sum(nums, target))

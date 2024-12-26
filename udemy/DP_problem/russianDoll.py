# def russianDoll(nums):
    
#     # n=len(nums)
#     nums.sort(key=lambda x:x[0])
#     #[[1,2], [4,3], [5,3], [5,6]]
#     result=[nums[0]]

#     for start, end in nums[1:]:
#         pstart=result[-1][0]
#         pend=result[-1][1]

#         if pstart<start and pend<end:
#             result.append([start, end])

#     return len(result)


# nums=[[4,3],[5,3],[5,6],[1,2]]
# print(russianDoll(nums))


def russianDoll(envolpes):
    
    # envolpes.sort(key=lambda x:x[0])
    # print(envolpes)
    envolpes.sort(key=lambda x:(x[0],-x[1]))
    # print(envolpes)

    n=len(envolpes)
    dp=[1]*n
    maxlength=1

    for i in range(1,n):
        for j in range(i):

            if envolpes[j][1]<envolpes[i][1] and dp[j]+1>dp[i]:
                dp[i]=dp[j]+1

        if dp[i]>maxlength:
            maxlength=dp[i]

    return maxlength



envolpes=[[1,2], [3,4], [5,5], [6,6], [3,6], [5,6]] 
#we can get o/p=2 or 3 or 4 always get the max o/p=4
print(russianDoll(envolpes))
def maxSubArray(nums):
    curr_max = nums[0]
    ans = nums[0]
    left, right, curr_left, curr_right = 0,0,0,0
    for i in range(1,len(nums)):
        if curr_max < 0:
            curr_max = nums[i]
            curr_left = curr_right = i
        else:
            curr_max += nums[i]
            curr_right += 1
        if ans < curr_max:
            ans = curr_max
            left = curr_left
            right = curr_right
    return left, right, ans
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
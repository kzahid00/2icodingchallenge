def challenge(nums, target):
    #to keep track of found pairs
    count = 0
    #pointers pointing at the start and at the end of the list
    ptr1 = 0
    ptr2 = len(nums) - 1
    
    #while the pointers don't cross each other or meet in the middle
    while ptr1 < ptr2:
        #if we find pairs that sum to the target, move both pointers in and increment the count
        if nums[ptr1] + nums[ptr2] == target:
            count+=1
            ptr1+=1
            ptr2-=1
        #if the sum is less than the target, we need a higher number, so move up the start pointer (to a higher number)
        elif nums[ptr1] + nums[ptr2] < target:
            ptr1+=1
        #if the sum is greater than the target, we need a smaller number, so move down the end pointer (to a lower number)
        elif nums[ptr1] + nums[ptr2] > target:
            ptr2-=1
    #return the final count of pairs            
    return count

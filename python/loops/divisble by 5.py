nums = [12, 75, 150, 180, 145, 525, 50]
for i in range (0,len(nums)):
    if((nums[i]%5)==0):
        if(nums[i]==150):
            pass
        else:
            print(nums[i])
            if (nums[i] > 500):
                break
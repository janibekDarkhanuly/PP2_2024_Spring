def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            print("True")
            return
    print("false")

has_33([1,3,2,1,3,2,1,2,3])
def spy_game(nums):
    has_zero1 = False
    has_zero2 = False
    has_seven = False

    for num in nums:
        if num == 0 and not has_zero1:
            has_zero1 = True
        elif num == 0 and has_zero1 and not has_zero2:
            has_zero2 = True
        elif num == 7 and has_zero1 and has_zero2:
            has_seven = True
            break  

    return has_zero1 and has_zero2 and has_seven
print(spy_game([1,2,4,0,0,1,5]))  
print(spy_game([1,0,2,4,0,2,1]))  
print(spy_game([1,7,2,0,4,5,0,2,1,2,3,4,5,1,2,3,4,2,1,2,34,12,123,123,123,2,23,0,0,7]))  

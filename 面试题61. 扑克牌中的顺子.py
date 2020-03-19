def isStraight(nums) -> bool:
    nums.sort()
    count = 0 
    for i in range(5):
        if nums[i] == 0:
            count += 1
    for i in range(4,count,-1):
        n = nums[i] - nums[i-1]
        if n != 1:
            count -= n - 1
            if count < 0:
                return False
    return True

if __name__ == "__main__":
    nums = [0,0,3,4,5]
    isStraight(nums)
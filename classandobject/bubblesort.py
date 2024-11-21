def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

def sort1(nums):

    small = nums[0]
    for i in range(0, len(nums) - 1):

        if (nums[i] < small):
            small=nums[i]

    print(small)


nums = [5, 8, 42, 99, 63, 77, 1, 5, 7, 6]
#sort(nums)
print(nums)

sort1(nums)
print()



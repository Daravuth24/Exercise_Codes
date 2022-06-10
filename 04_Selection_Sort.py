# Sort from the right to left
def selection_sort(nums):
    for i in range(len(nums)-1, -1, -1): # From the last index to the first index, with an increment of -1
        max = i
        for j in range(0, i):
            if nums[j] > nums[max]:
                max = j
        nums[i], nums[max] = nums[max], nums[i]
        print(nums)



selection_sort([51, 25, 65, 6, 78])

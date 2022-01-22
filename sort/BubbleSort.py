def bubble_sort(nums):
  for i in range(len(nums)):
    for j in range(len(nums)-1, i, -1):
      if nums[j] < nums[j-1]:
        nums[j], nums[j-1] = nums[j-1], nums[j]

  return nums


a = [5, 3, 2, 1, 4]
print(bubble_sort(a))
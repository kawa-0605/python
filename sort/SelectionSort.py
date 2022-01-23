def selection_sort(nums):
  for i in range(0, len(nums)):
    minj = i
    for j in range(i, len(nums)):
      if nums[j] < nums[minj]:
        minj = j
    nums[i], nums[minj] = nums[minj], nums[i]

  return nums


a = [5, 3, 2, 1, 4]
print(selection_sort(a))
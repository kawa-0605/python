def insertion_sort(nums):
  for i in range(1, len(nums)):
    v = nums[i]
    j = i - 1
    
    while (j >= 0 and nums[j] > v):
      nums[j+1] = nums[j]
      j -= 1
    nums[j+1] = v
  
  return nums


a = [4, 42, 14, 7, 1]
print(insertion_sort(a))
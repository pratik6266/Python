# while loop
nums = [23, -45, 67, -12, 89, -34, 0, 56, -78, 14]

count = 0
i = 0

while i < len(nums):
  if nums[i] == 0:
    i = i + 1
    continue
  elif nums[i] < 0:
    count = count + 1
  i = i+1

print(count)


# for loops
for i in range(0, len(nums)):
  if i == 5:
    break 
  print(nums[i], end=" ")

print()

# for loops for list 
for num in nums:
  print(num, end=" ")


# do while loops do not exits in python


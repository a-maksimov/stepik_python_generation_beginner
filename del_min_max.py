# put your python code here

n = int(input())

nums = []
maximum = -10**6
minimum = 10**6
max_index = 0
min_index = 0

for i in range(n):
    num = int(input())
    nums.append(num)

for i in range(len(nums)):
    if nums[i] >= maximum:
        maximum = nums[i]
        max_index = i
del nums[max_index]
for i in range(len(nums)):
    if nums[i] <= minimum:
        minimum = nums[i]
        min_index = i
del nums[min_index]

print(*nums, sep='\n')
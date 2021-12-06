
# Advent of Code 2021 Day 6
# https://adventofcode.com/2021/day/6

def readData():
    with open('sample.txt') as f:
      nums = f.read().split(",")
      # map will apply the int function to all values in nums... int can be any function
      for i in range(len(nums)):
        nums[i] = int(nums[i])
      # nums = map(int, nums)
      
        # lines = f.read().splitlines()
      
      return nums

def part1(nums):
  days = 80

  for i in range(days):
    for j in range(len(nums)):
      fish = nums[j]
      if fish == 0:
        nums.append(8)
        nums[j] = 6
      else:
        nums[j] -= 1
  
  return len(nums)

def part2(nums):
  print(nums)
  days = 256

  for i in range(days):
    for j in range(len(nums)):
      fish = nums[j]
      if fish == 0:
        nums.append(8)
        nums[j] = 6
      else:
        nums[j] -= 1
  
  return len(nums)


nums = readData()  
print(nums)
part1Answer = part1(nums)
print("Part1 Answer: " + str(part1Answer))

# reset Nums
nums = readData()
part2Answer = part2(nums)
print("Part2 Answer: " + str(part2Answer))



# part1(lines)
# part2(lines)

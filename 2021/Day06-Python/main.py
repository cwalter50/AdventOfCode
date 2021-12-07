
# Advent of Code 2021 Day 6
# https://adventofcode.com/2021/day/6

def readData():
    with open('data.txt') as f:
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

def totalChildren(daysLeft, startNum):
  total = 0
  if (daysLeft >= startNum):
    total += int(daysLeft - startNum) // 6
    total += totalChildren(daysLeft-startNum, 8)
  
  # print("total children: " + str(total))
  return total

# Try Dennis's algorithm. 
# keep track of how many fish are at each day in the cycle and store those values in an array
# ie [5, 4, 2, 1, 5, 6, 7, 2, 9] There are 5 fish on day 0, 4 fish on day 1, etc. 
# rotate the array to the left 256 times, each time adding more fish to day 6 or day 8. 
# sum total fish in array at the end

def rotateFish1Day(fish):
  temp = fish[0]
  for i in range(1, 9):
    fish[i-1] = fish[i]
  
  fish[6] += temp
  fish[8] = temp

  return fish

  
def part2(nums):
  days = 256

  fish = [0,0,0,0,0,0,0,0,0]
  for num in nums:
    fish[num] += 1
  # print(fish)

  for i in range(days):
    fish = rotateFish1Day(fish)

  return sum(fish)

nums = readData()  
print(nums)
part1Answer = part1(nums)
print("Part1 Answer: " + str(part1Answer))

# reset Nums
nums = readData()
part2Answer = part2(nums)
print("Part2 Answer: " + str(part2Answer))


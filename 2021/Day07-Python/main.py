# Advent of Code 2021 Day 7
# https://adventofcode.com/2021/day/7

def readData():
    with open('data.txt') as f:
      nums = f.read().split(",")
      # map will apply the int function to all values in nums... int can be any function
      for i in range(len(nums)):
        nums[i] = int(nums[i])
      # nums = map(int, nums)
      
        # lines = f.read().splitlines()
      
      return nums
    
    # here is a comment

def part1(nums):
  # loop from min to max of data
  minNum = min(nums)
  maxNum = max(nums)
  minTotal = 10000000000000
  for i in range(minNum, maxNum+1):
    total = 0
    for num in nums:
      # find distance from num to i and add to total
      total += abs(num - i)
    if total < minTotal:
      minTotal = total
  return minTotal

# returns the sum from 1 to num
def summation(num):
  sum = 0
  for i in range(num+1):
    sum += i
  return sum


def part2(nums):
  # loop from min to max of data
  minNum = min(nums)
  maxNum = max(nums)
  minTotal = 10000000000000
  for i in range(minNum, maxNum+1):
    total = 0
    for num in nums:
      # find distance from num to i and add to total
      total += summation(abs(num - i))
    if total < minTotal:
      minTotal = total
  return minTotal


nums = readData()  
# print(nums)

part1Answer = part1(nums)
print("Part 1 Answer: " + str(part1Answer))

# # reset Nums
# nums = readData()
part2Answer = part2(nums)
print("Part2 Answer: " + str(part2Answer))
